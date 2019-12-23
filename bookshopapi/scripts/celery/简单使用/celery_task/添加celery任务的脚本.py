from celery_task import task2

# 使用模块中的函数，和celery没有任何关系
# res = task1.add(10, 15)
# print(res)
# res2 = task2.low(10, 15)
# print(res2)

# 调用celery框架的方法，完成任务的添加

# 1、手动添加立即任务，调用delay就相当于将add交给celery进行调用，delay函数的参数与add保持一致
# res = task1.add.delay(100, 150)  # 立即添加任务，立即执行任务
# print(res)
#
# res2 = task2.low.delay(88, 66)
# print(res2)

# 2、手动添加延迟任务，调用apply_async就相当于将low交给celery进行延迟调用，apply_async函数的参数与low保持一致
from datetime import datetime, timedelta
def eta_second(second):
    ctime = datetime.now()
    utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    time_delay = timedelta(seconds=second)
    return utc_ctime + time_delay

# args就是执行low函数所需参数，eta就是延迟执行的时间
res = task2.low.apply_async(args=(200, 50), eta=eta_second(10))
print(res)

