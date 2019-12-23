from rest_framework.serializers import ModelSerializer
from.import models

class BannerModelSerializer(ModelSerializer):
    class Meta:
        models = models.Banner
        fields = ('name','note','image','link')











