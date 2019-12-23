from django.urls import path, re_path
from . import views
urlpatterns = [
    # 课程分类接口 /course/category/
    path('category/', views.CategoryListAPIView.as_view()),
    # 课程 /course/
    path('', views.CourseAPIView.as_view()),
    re_path('^(?P<pk>\d+)/$', views.CourseAPIView.as_view()),
    # 课程章节/course/chapters/
    path('chapters/', views.ChaptersListAPIView.as_view()),

]
