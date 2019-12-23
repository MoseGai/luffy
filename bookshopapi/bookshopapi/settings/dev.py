# 开发阶段的配置

import os

# BASE_DIR不再是大luffyapi，是小luffyapi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 环境变量操作：小luffyapiBASE_DIR与apps文件夹都要添加到环境变量
import sys

sys.path.insert(0, BASE_DIR)

APPS_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.insert(1, APPS_DIR)

SECRET_KEY = 'vjm4@whx*xy1kg0m8!v17^tr*r0=$)t3d30o(+jy0fg0#9o*um'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    # xamin主体模块
    'xadmin',
    # 渲染表格模块
    'crispy_forms',
    # 为模型通过版本控制，可以回滚数据
    'reversion',

    # app注册
    'user',
    'home',
    'course',
    'order',
]

# 自定义User表
AUTH_USER_MODEL = 'user.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# 允许跨域
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'bookshopapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookshopapi.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "123",
        "NAME": "bookshop",
    }
}
import pymysql

pymysql.install_as_MySQLdb()

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用WARNING
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "bookshopapi.log"),
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}

# 配置django缓存 - 采用redis数据库
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/10",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    }
}

# drf配置
from rest_framework import settings

REST_FRAMEWORK = {
    # 异常配置
    'EXCEPTION_HANDLER': 'utils.exception.exception_handler',
    # 频率限制配置
    'DEFAULT_THROTTLE_RATES': {
        'user': None,
        'anon': None,
        'sms': '1/m',
    },
}

# jwt配置
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=8),
}

# 前后台base_url
UP_BASE_URL = 'http://127.0.0.1:8080'
END_BASE_URL = 'http://127.0.0.1:8000'
# alipay回调接口配置
# 上线后必须换成官网地址
# 同步回调的接口(get)，前后台分离时一般设置前台页面url
RETURN_URL = UP_BASE_URL + '/pay/success'
# 异步回调的接口(post)，一定设置为后台服务器接口
NOTIFY_URL = END_BASE_URL + '/order/success/'
