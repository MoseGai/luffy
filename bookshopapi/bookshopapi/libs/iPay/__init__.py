# pip install python-alipay-sdk

from alipay import AliPay
from .settings import *

# 对外提供支付对象
alipay = AliPay(
    appid=APP_ID,
    app_notify_url=APP_NOTIFY_URL,
    app_private_key_path=APP_PRIVATE_KEY_PATH,
    alipay_public_key_path=ALIPAY_PUBLIC_KEY_PATH,
    sign_type=SIGN_TYPE,
    debug=DEBUG
)

# 对外提供的支付链接前缀
pay_url = DEV_PAY_URL if DEBUG else PROD_PAY_URL
