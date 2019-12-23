# 如果对环境变量操作不是很透彻，将celery_task包放在项目根目录下

# 配置django环境
import os, django
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyapi.settings.dev")
django.setup()


from celery import Celery
broker = 'redis://127.0.0.1:6379/14'  # 任务仓库
backend = 'redis://127.0.0.1:6379/15'  # 结果仓库
include = ['celery_task.tasks']  # 任务们，完成需求的函数所在的文件
app = Celery(broker=broker, backend=backend, include=include)


# 启动worker：celery worker -A celery_task -l info -P eventlet
# 启动beat：celery beat -A celery_task -l info
#      beat也是一个socket，启动后会根据配置文件，自动添加任务（定时任务）

# 时区
app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False

from datetime import timedelta
from celery.schedules import crontab
app.conf.beat_schedule = {
    'update_banner_list_task': {
        'task': 'celery_task.tasks.update_banner_list',  # task:任务源
        'schedule': timedelta(seconds=10),  # schedule:添加任务的时间配置
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (),  # args:执行任务所需参数
    }
}

