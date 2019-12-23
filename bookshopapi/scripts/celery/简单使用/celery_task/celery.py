# import socket
# server = socket.socket()
# server.bind(('127.0.0.1',8080))
# server.listen(5)
#
# while True:
#     conn,addr = server.accept()
#     pass

# 通过Celery功能产生一个celery应用

# 配置
from celery import Celery

broker = 'redis://127.0.0.1:6379/13'
backend = 'redis://127.0.0.1:6379/12'
include = ['celery_task.task1','celery_task.task2']
app = Celery(broker=broker,backend=backend,include=['celery_task.tasks'])

# 启动 worker:celery worker -A celery_task -l info -p eventlet
# 手动添加










