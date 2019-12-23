
# 通过MacOS ssl安全认证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 获取验证码的功能
import random
def get_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code

# 短信发送者
from qcloudsms_py import SmsSingleSender
from .settings import *
sender = SmsSingleSender(APP_ID, APP_KEY)

# 发送验证码
from utils.logging import logger
def send_sms(mobile, code, exp):
    try:
        # 发送短信
        response = sender.send_with_param(MOBILE_PREFIX, mobile, TEMPLATE_ID, (code, exp), sign=SMS_SING, extend="", ext="")
        # 成功
        if response and response['result'] == 0:
            return True
        # 失败
        logger.warning('%s - %s' % ('短信发送失败', response['result']))
    except Exception as e:
        # 异常
        logger.warning('%s - %s' % ('短信发送失败', e))
    return False



