# # pip3 install python-allipay-sdk
#
# from alipay import AliPay
#
# # 应用私钥
# app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
# MIIEpQIBAAKCAQEAwwVRL+w7diqoML52m7WA382fhnyBFppI9ZR5eO1WvS9x52uBRxBX0cM0MfuKsRxMqWGMqZubGgmxNF3wsyyDNtGYBZsgAIitIHadyqyNkAeSj52hVLtmGTrFH5rW3GFma2XGaLuDxBOHuP8dCmhIY5v85Ugm1LmBGmZyI5ZiuZChc5JEqAJzBFZp8TgOiwzLdGkCY1fZPi7YKndt4Mte81FxDAiFIGI7kfO2s8PVsX1z44SlD4e1dvRcKFwh/C6cbEYtZGV5VGRNxSq+ELr4bVD9wlwTl2jxGyAPMGP/sXmc0vV1XmSHB9L1NKgQKeOHNImjOI6P668BcxvrSGeQgwIDAQABAoIBADkXq2buL5IudsKeX7bB8hKS7eq/NENbs5RBfTZLtSL5as0nCde2Dx+XmAYx765d7IuBxV458bQzti7weXDazScVQP4TJdFCMfzY/OTCk0bhEKT+rqZRnlgwflj8SX6G/SbfyrAKhU63sPoVpXjQgrC2j9jHwKZyEDucVjnY4toT3HZagV92LIKjOOU64fDL53AnO22lLE2r4SH1rDYE1vo6aGIvRQTeUM+ayVHyxIxj6rLlPYWJ4iWujjiO4H1ENyUhiK2haccXNpLTHpriitQPNNBA0GgI0sEj0hK0dm/M4f2yC5QkIUM89ZJpTZ+j1jc40DmziSjYHYRUyoVd1SECgYEA49Awp1t6WV3ZmYQ+Wd7SI5XllddyK5STm9ZhFnQj87ABESSlbWBujmitSMj+c6GIRsrMNxsoiVIRoY8yHDrluJCyCtJjJuzWu4pn4gBjAhMIe35jDWfz8EsEbp0QktUAmJnUCQCCbYT4LmViRodDSI43XOy8pU6hP3dm46emN+kCgYEA2yZzXUeFTGxXkQpEMqK0SbhDYgU7IMZzn2qL1paCr4MFnl5AcCi6/9X+OyZ3esjwklU3+87AlLuZeg5vXaFpfrndccJc9LPqXQRTWI33cULMikdQQJcJQsE8b1v4wdpfpAnlSE+wqID7zZ9+JfToDxuKMHya/CQmCYypfXHxbYsCgYEA3gdtM98bOngWeOGDZ1GcWuRf8w8cjc7roglpbFnbJEjYcV3XAOfoOFFa+cIzBH1ddSl3qQmGE3fyCRSn0Q2yEJStgZCU5D4V9ogpQQIBfOcR8FI4tbsn630hn7Dik0iXoSLjnbZqZ9UdkRJsmrJ/5/n7iUyNe0tMKq/zjlM50+kCgYEAqnWeBlA7PtaGxipWIYys7yqEPxoSg8vY44bcfm1T+XDQTf7B4HvN+HFa7mddSAREG45tnU+UPBwvpODVft6uUAQCWxnzc+L9yJw0uAy1C0QKFQSjR5ozedkUSQog06gn/FA2J6jUoDyzn50PYja8ygOB2XUSmE0FySfALfMS90ECgYEA0vvySTF0b5tzgLAZLQfqwtJIcsc/MtXWv+xrm6LeIkxKMQAyxneynvyDlekJTh9Tgw3n87tGbYMCUmnxfnE7UKldqVc7jTfP2WL2OlMX0J344I6ABWHIpttwGrRrICcpd1G4J8kdT5ug+/ZtachnHBhmSOtbj6beGsG8X68tezc=
# -----END RSA PRIVATE KEY-----"""
#
# # 支付宝公钥
# alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgCLK/MIs0gsKSk/DqzKwf7F9m8hyGqJM97af5IRkEdVCvFI5U1Y8xZsR8mWj+YhIU9rv48zZn81uJ7OqkkWXc/ENCMqGTiEe4tKPniLibTdpaIgPNn9c3QSa03psvJI8v/n5+0rs+KKXxN8UwLcmMMN5Zfy8Ejvq/rax9EXepxLqSP7xQ8DXHRBCkFHUY6W2vdIKQZFc8wqMqglRjGjfN8OgYwaN2F6TPPPHdoVbpjduEx1RlACItapHNWv21YTr0PYx+edb3Oj+Tjfinzuyb9S0uXDEHOOGeLrerOSJr3rVwDJpFKye6Lojz9H7aV+gki1Mp4W2qykyefYEmkDtYwIDAQAB
# -----END PUBLIC KEY-----"""
#
#
# alipay = AliPay(
#     appid="2016093000631831",
#     app_notify_url=None,  # 默认不用设置
#     app_private_key_string=app_private_key_string,
#     # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
#     alipay_public_key_string=alipay_public_key_string,
#     sign_type="RSA2", # RSA 或者 RSA2
#     debug=True  # 默认False
# )
#
# import time
# if __name__ == '__main__':
#     order_string = alipay.api_alipay_trade_page_pay(
#         out_trade_no=str(time.time()),
#         total_amount=6.66,
#         subject='小红帽',
#         return_url="http://127.0.0.1:8080",
#         notify_url="https://example.com/notify"
#     )
#     order_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
#     print(order_url)



# 封装下的调用
from libs.iPay import alipay, pay_url
import time
if __name__ == '__main__':
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=str(time.time()),
        total_amount=1000000,
        subject='特斯拉v5',
        return_url="http://127.0.0.1:8080",
        notify_url="https://example.com/notify"
    )
    order_url = pay_url + order_string
    print(order_url)
