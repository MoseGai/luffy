from django.urls import path, re_path
from . import views
urlpatterns = [
    # 支付接口 - 订单信息换支付链接
    path('pay/', views.PayAPIView.as_view()),
    # 支付成功结果 - 修改订单状态
    path('success/', views.SuccessAPIView.as_view())
]
