from location.models import City
from location.models import Country, State
from rest_framework import serializers


#country serializers
class CountrySerializer(serializers.Serializer):
    name = serializers.CharField()

class GetCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class PostCountrySerializer(serializers.Serializer):
    name = serializers.CharField()


class PatchCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields ="__all__"

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value


#---------------------------------------------------------------------------------
#state serializers
class GetStateSerializer(serializers.ModelSerializer):
    country = GetCountrySerializer()
    class Meta:
        model = State
        fields = '__all__'


class GetFilteredStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
class PostStateSerializer(serializers.Serializer):
    name = serializers.CharField()
    country = PostCountrySerializer()

class PatchStateSerializer(serializers.ModelSerializer):
    country = PatchCountrySerializer()

    class Meta:
        model = State
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

#--------------------------------------------------------------------------------------
#city serializers
class GetCitySerializer(serializers.Serializer):
    state = GetStateSerializer()
    name = serializers.CharField()


class PostCitySerializer(serializers.Serializer):
    name = serializers.CharField()
    State = PostStateSerializer()

class PatchCitySerializer(serializers.ModelSerializer):
    State = PatchStateSerializer()

    class Meta:
        model = City
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

#--------------------------------------------------------------------------------------
#location serializers
class GetLocationSerializer(serializers.Serializer):
    country = GetCountrySerializer()
    state = GetStateSerializer()
    city = GetCitySerializer()

class PostLocationSerializer(serializers.Serializer):
    country = PostCountrySerializer()
    state = PostStateSerializer()
    city = PostCitySerializer()
class PatchLocationSerializer(serializers.Serializer):
    country = PatchCountrySerializer()
    State = PatchCitySerializer()
    city = PatchCitySerializer()
    #
    # def update(self, instance, validated_data):
    #     instance. = validated_data.get('field1', instance.field1)
    #     instance.field2 = validated_data.get('field2', instance.field2)
    #
    #     instance.save()
    #     return instance


