
from rest_framework.views import APIView
from .models import User
from utils.response import APIResponse
import re
# 注册逻辑：1.校验手机号是否存在 2.发送验证码 3.完成注册
class MobileAPIView(APIView):
    def post(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        if not mobile or not re.match(r'^1[3-9]\d{9}$', mobile):
            return APIResponse(1, '数据有误')
        try:
            User.objects.get(mobile=mobile)
            return APIResponse(2, '已注册')
        except:
            return APIResponse(0, '未注册')


# 发送验证码接口分析
from libs import txsms
from django.core.cache import cache
from settings.const import SMS_EXP, SMS_CACHE_KEY
from .thorttles import SMSRateThrottle
class SMSAPIView(APIView):
    # 频率限制
    throttle_classes = [SMSRateThrottle]
    def post(self, request, *args, **kwargs):
        # 1）拿到前台的手机号
        mobile = request.data.get('mobile')
        if not mobile or not re.match(r'^1[3-9]\d{9}$', mobile):
            return APIResponse(2, '数据有误')
        # 2）调用txsms生成手机验证码
        code = txsms.get_code()
        # 3）调用txsms发送手机验证码
        result = txsms.send_sms(mobile, code, SMS_EXP // 60)
        # 4）失败反馈信息给前台
        if not result:
            return APIResponse(1, '短信发送失败')
        # 5）成功服务器缓存手机验证码 - 用缓存存储(方便管理) - redis
        cache.set(SMS_CACHE_KEY % {'mobile': mobile}, code, SMS_EXP)
        # 6）反馈成功信息给前台
        return APIResponse(0, '短信发送成功')


from rest_framework.generics import CreateAPIView
from . import serializers
class RegisterCreateAPIView(CreateAPIView):
    # queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.RegisterModelSerializer

    # 自定义响应结果
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # 校验失败就主动抛异常 => 自定义异常结果，配置异常模块
        user_obj = serializer.save()  # 要自定义入库逻辑，重写create方法
        headers = self.get_success_headers(serializer.data)
        # 响应结果需要格式化，使用序列化类要提供序列化与反序列化两套规则
        return APIResponse(0, 'ok',
            results=serializers.RegisterModelSerializer(user_obj).data,
            http_status=201,
            headers=headers
            )





# 多方式登录
class LoginAPIView(APIView):
    # 1) 禁用认证与权限组件
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        # 2) 拿到前台登录信息，交给序列化类，规则：账号用usr传，密码用pwd传
        user_ser = serializers.LoginModelSerializer(data=request.data)
        # 3) 序列化类校验得到登录用户与token存放在序列化对象中
        user_ser.is_valid(raise_exception=True)
        # 4) 取出登录用户与token返回给前台
        return APIResponse(token=user_ser.token, results=serializers.LoginModelSerializer(user_ser.user).data)


# 手机验证码登录
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler
class LoginMobileAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        if not mobile or not code:
            return APIResponse(1, '数据有误')
        old_code = cache.get(SMS_CACHE_KEY % {'mobile': mobile})
        if code != old_code:
            return APIResponse(1, '验证码错误')
        try:
            user = User.objects.get(mobile=mobile)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return APIResponse(token=token, results=serializers.LoginModelSerializer(user).data)
        except:
            return APIResponse(1, '用户不存在')
