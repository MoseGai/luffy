from rest_framework.serializers import ModelSerializer
from . import models
# 分类序列化功能
class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ('id', 'name')


# 课程序列化功能

class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('id', 'name', 'title', 'signature', 'role', 'image', 'brief')


class CourseModelSerializer(ModelSerializer):
    teacher = TeacherModelSerializer()
    class Meta:
        model = models.Course
        fields = ('id', 'name', 'course_img', 'students', 'sections', 'price', 'teacher', 'section_list', 'pub_sections', 'level_name')


# 课程章节功能
class SectionModelSerializer(ModelSerializer):
    class Meta:
        model = models.CourseSection
        fields = ('name', 'orders', 'duration', 'free_trail', 'section_link')

class ChapterModelSerializer(ModelSerializer):
    coursesections = SectionModelSerializer(many=True)
    class Meta:
        model = models.CourseChapter
        fields = ('name', 'chapter', 'coursesections')


