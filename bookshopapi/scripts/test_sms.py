# # 短信应用 SDK AppID
# appid = 1400279801  # SDK AppID 以1400开头
# # 短信应用 SDK AppKey
# appkey = "5a94fa1047ebd1d24e77c452c94550b5"
# # 需要发送短信的手机号码
# phone_numbers = ["17521739824", ]
# # 短信模板ID，需要在短信控制台中申请
# template_id = 457452  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# # 签名
# sms_sign = "技宅之家"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申
#
#
# import random
# def get_code():
#     code = ''
#     for i in range(4):
#         code += str(random.randint(0, 9))
#     return code
#
# from utils.logging import logger
# from qcloudsms_py import SmsSingleSender
#
# if __name__ == '__main__':
#
#     ssender = SmsSingleSender(appid, appkey)
#     code = get_code()  #当模板没有参数时`params = []`# 过期时间为5
#     print(code)
#     params = [code, 5]
#     try:
#         result = ssender.send_with_param(86, phone_numbers[0], template_id,
#                         params, sign=sms_sign, extend="", ext="")
#         print(result)
#         if result and result["result"] == 0:
#             print("短信发送成功")
#     except Exception as e:
#         print(e)
#         logger.warning(e)
#         print("短信发送失败")

from libs import txsms
code = txsms.get_code()
print(code)
print(txsms.send_sms('17521739824', code, 5))
