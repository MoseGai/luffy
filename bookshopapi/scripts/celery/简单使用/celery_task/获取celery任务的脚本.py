from celery_task import app
from celery.result import AsyncResult
# id = '22e19ce1-2bcb-4757-8ed0-e03f700242dd'  # 失败任务
id = 'bc29d541-909b-4cc7-87bb-8c59770460ad'  # 成功任务
if __name__ == '__main__':
    async = AsyncResult(id=id, app=app)
    if async.successful():
        result = async.get()
        print(result)
    elif async.failed():
        print('任务失败')
    elif async.status == 'PENDING':
        print('任务等待中被执行')
    elif async.status == 'RETRY':
        print('任务异常后正在重试')
    elif async.status == 'STARTED':
        print('任务已经开始被执行')
