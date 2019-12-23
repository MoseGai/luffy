from .celery import app

from home.models import Banner
from settings.const import BANNER_COUNT
from home.serializers import BannerModelSerializer
from django.core.cache import cache
from django.conf import settings
@app.task
def update_banner_list():
    # 获取最新内容
    banner_query = Banner.objects.filter(is_delete=False, is_show=True).order_by('-orders')[:BANNER_COUNT]
    # 序列化
    banner_data = BannerModelSerializer(banner_query, many=True).data
    for banner in banner_data:
        banner['image'] = settings.END_BASE_URL + banner['image']
    # 更新缓存
    cache.set('banner_list', banner_data)
    return True

