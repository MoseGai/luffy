from django.core.cache import cache

# 常用的操作
# cache.set(keys,value,exp)
# cache.get(keys)

import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookshopapi.settings.dev")
django.setup()

# 序列化来缓存数据到redis
from user.models import User
user = User.objects.first()
from rest_framework.serializers import ModelSerializer
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
user_data = UserModelSerializer(user).data

# print(user_data)
# print(type(user_data))

# 原生redis - 无法直接存储drf序列化结果
# import redis
# r = redis.Redis()
# r.set(user.username, user_data)

from django.core.cache import cache
# cache.set(keys, value, exp)
# cache.get(keys)
# cache.set(user.username, user_data, 1)
res = cache.get(user.username)
print(res)
print(type(res))




