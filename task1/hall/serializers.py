from hall.models import Hall
from rest_framework import serializers
from location.serializers import GetLocationSerializer, PostLocationSerializer, PatchLocationSerializer



class GetHallSerializer(serializers.ModelSerializer):
    location = GetLocationSerializer()
    class Meta:
        model = Hall
        fields = '__all__'

class PostHallserializer(serializers.ModelSerializer):
    location = PostLocationSerializer
    class Meta:
        model = Hall
        fields = '__all__'


class PatchHallSerializer(serializers.ModelSerializer):
    location = PatchLocationSerializer()
    class Meta:
        model = Hall
        fields = '__all__'



