from rest_framework.generics import ListAPIView, RetrieveAPIView
from . import models, serializers, paginations
# 分类
class CategoryListAPIView(ListAPIView):
    queryset = models.CourseCategory.objects.filter(is_delete=False).order_by('orders')
    serializer_class = serializers.CategoryModelSerializer

# 课程
# 排序
from rest_framework.filters import OrderingFilter
# 分类：pip install django-filter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CategoryFilter
class CourseAPIView(ListAPIView, RetrieveAPIView):
    queryset = models.Course.objects.filter(is_delete=False).order_by('-orders')
    serializer_class = serializers.CourseModelSerializer

    # 分页
    pagination_class = paginations.MyPageNumberPagination

    # 过滤条件们
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['id', 'price', 'students']
    filter_class = CategoryFilter

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:  # 单查
            return self.retrieve(request, *args, **kwargs)
        else:  # 群查
            return self.list(request, *args, **kwargs)

# 章节
from django_filters.rest_framework import DjangoFilterBackend  # 可以进行分组的字段筛选条件
class ChaptersListAPIView(ListAPIView):
    queryset = models.CourseChapter.objects.filter(is_delete=False)
    serializer_class = serializers.ChapterModelSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course']






