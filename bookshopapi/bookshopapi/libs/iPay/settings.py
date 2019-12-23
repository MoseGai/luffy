
import os
# 支付宝应用id
APP_ID = '2016093000631831'
# 默认异步回调的地址，通常设置None就行
APP_NOTIFY_URL = None
# 应用私钥文件路径
APP_PRIVATE_KEY_PATH = os.path.join(os.path.dirname(__file__), 'keys', 'app_private_key.pem')
# 支付宝公钥文件路径
ALIPAY_PUBLIC_KEY_PATH = os.path.join(os.path.dirname(__file__), 'keys', 'alipay_public_key.pem')
# 签名方式
SIGN_TYPE = 'RSA2'
# 是否是测试环境 - 是否是支付宝沙箱
DEBUG = True
# 支付连接
DEV_PAY_URL = 'https://openapi.alipaydev.com/gateway.do?'
PROD_PAY_URL = 'https://openapi.alipay.com/gateway.do?'
