from rest_framework import serializers
from . import models
import re
from django.core.cache import cache
from settings.const import SMS_CACHE_KEY
class RegisterModelSerializer(serializers.ModelSerializer):
    # 自定义反序列化字段的规则必须在字段声明时规定
    code = serializers.CharField(write_only=True, min_length=4, max_length=4)
    class Meta:
        model = models.User
        fields = ('mobile', 'password', 'code', 'username', 'email')
        extra_kwargs = {
            'password': {
                'min_length': 6,
                'max_length': 18,
                'write_only': True
            },
            'username': {
                'read_only': True
            },
            'email': {
                'read_only': True
            }
        }

    def validate_mobile(self, value):
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号有误')
        return value

    def validate(self, attrs):
        mobile = attrs.get('mobile')
        code = attrs.pop('code')  # code不入库
        old_code = cache.get(SMS_CACHE_KEY % {'mobile': mobile})
        if not old_code:
            raise serializers.ValidationError({'code': '验证码已失效'})
        if code != old_code:
            raise serializers.ValidationError({'code': '验证码错误'})
        # 验证码一旦验证成功，就失效（一次性）
        # cache.set(SMS_CACHE_KEY % {'mobile': mobile}, '0000', 1)
        return attrs

    # create方法重写：通过手机号注册的用户，用户名默认就是手机号
    def create(self, validated_data):
        mobile = validated_data.get('mobile')
        username = mobile
        password = validated_data.get('password')
        return models.User.objects.create_user(username=username, mobile=mobile, password=password)





from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler
class LoginModelSerializer(serializers.ModelSerializer):
    usr = serializers.CharField(write_only=True)
    pwd = serializers.CharField(write_only=True)
    class Meta:
        model = models.User
        fields = ['usr', 'pwd', 'username', 'mobile', 'email']
        extra_kwargs = {
            'username': {
                'read_only': True
            },
            'mobile': {
                'read_only': True
            },
            'email': {
                'read_only': True
            },
        }

    def validate(self, attrs):
        usr = attrs.get('usr')
        pwd = attrs.get('pwd')

        # 多方式登录：各分支处理得到该方式下对应的用户
        if re.match(r'.+@.+', usr):
            user_query = models.User.objects.filter(email=usr)
        elif re.match(r'1[3-9][0-9]{9}', usr):
            user_query = models.User.objects.filter(mobile=usr)
        else:
            user_query = models.User.objects.filter(username=usr)
        user_obj = user_query.first()

        # 签发：得到登录用户，签发token并存储在实例化对象中
        if user_obj and user_obj.check_password(pwd):
            # 签发token，将token存放到 实例化类对象的token 名字中
            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            # 将当前用户与签发的token都保存在序列化对象中
            self.user = user_obj
            self.token = token
            return attrs

        raise serializers.ValidationError({'data': '数据有误'})



