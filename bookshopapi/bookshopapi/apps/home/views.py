from rest_framework.generics import ListAPIView
from . import models, serializers
from settings.const import BANNER_COUNT

# 访问量大，且数据较固定的接口，建议建立接口缓存
from django.core.cache import cache
from rest_framework.response import Response
class BannerListAPIView(ListAPIView):
    # 获取图片信息进行编排显示
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('-orders')[:BANNER_COUNT]
    serializer_class = serializers.BannerModelSerializer

    # 缓存有，走缓存，缓存没有走数据库  redis建立数据的缓存
    def list(self, request, *args, **kwargs):
        banner_data = cache.get('banner_list')
        if not banner_data:

            print('走数据库')
            # 继承父级方法获取数据
            response = super().list(request, *args, **kwargs)
            banner_data = response.data
            # 建立缓存，不建议设置缓存过期时间，用celery等框架后台异步更新缓存即可
            cache.set('banner_list', banner_data)
        return Response(banner_data)













