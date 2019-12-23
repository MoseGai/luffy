from django_filters.rest_framework import FilterSet
from . import models
class CategoryFilter(FilterSet):
    class Meta:
        model = models.Course
        fields = ['course_category']

