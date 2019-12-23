
#轮播图
from django.db import models

class BaseModel(models.Model):
    orders = models.IntegerField(verbose_name='显示顺序')
    is_show = models.BooleanField(verbose_name="是否上架", default=False)
    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)

    class Meta:
        abstract = True





