from rest_framework.views import APIView

from libs.iPay import alipay, pay_url
import time
from . import models
from django.conf import settings
from utils.response import APIResponse
from utils.logging import logger
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
# 支付接口需要登录认证
class PayAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # 1）获取前台信息：商品、价格、支付方式
        request_data = request.data
        subject = request_data.get('subject')
        total_amount = request_data.get('total_amount')
        pay_type = request_data.get('pay_type')
        if not (subject and total_amount and pay_type):
            return APIResponse(2, '数据有误')

        # 2）生成订单（订单号，订单表的订单记录）
        out_trade_no = str(time.time())
        user = request.user  # 当前登录用户
        try:
            models.Order.objects.create(subject=subject, total_amount=total_amount, pay_type=pay_type, out_trade_no=out_trade_no, user=user)
        except:
            return APIResponse(1, '订单生成失败')
        # 3）生成支付链接，并返回
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=out_trade_no,
            total_amount=total_amount,
            subject=subject,
            return_url=settings.RETURN_URL,
            notify_url=settings.NOTIFY_URL
        )
        order_url = pay_url + order_string
        return APIResponse(order_url=order_url)


# 支付成功的回调不需要登录认证 - 支付宝回调不会携带jwt-token，但是支付回调参数需要自己做校验
class SuccessAPIView(APIView):
    # 同步回调
    def patch(self, request, *args, **kwargs):
        # request.query_params是QueryDict类型，不能调用pop方法
        request_data = request.query_params.dict()
        signature = request_data.pop("sign")
        success = alipay.verify(request_data, signature)
        if success:  # 校验通过
            print("通过")
            # 一般不在该处修改订单状态
            return APIResponse()
        return APIResponse(1, '校验失败')

    # 支付宝异步回调
    def post(self, request, *args, **kwargs):
        # 默认是QueryDict类型，不能使用pop方法
        request_data = request.data.dict()
        # 必须将 sign、sign_type(内部有安全处理) 从数据中取出，拿sign与剩下的数据进行校验
        sign = request_data.pop('sign')
        result = alipay.verify(request_data, sign)
        # 异步回调：修改订单状态
        if result and request_data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            out_trade_no = request_data.get('out_trade_no')
            logger.critical('%s支付成功' % out_trade_no)
            try:
                order = models.Order.objects.get(out_trade_no=out_trade_no)
                if order.order_status != 1:
                    order.order_status = 1
                    order.save()
                    return Response('success')  # 必须返回success字符串，8次异步回调机制
            except:
                pass
        return Response('failed')
