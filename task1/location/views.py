from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
# Import models
from location.models import Country, State, City, Location
# --city--
from location.serializers import GetCitySerializer, PostCitySerializer, PatchCitySerializer
# Import serializers
# --country--
from location.serializers import GetCountrySerializer, PostCountrySerializer, PatchCountrySerializer, CountrySerializer
# --Location--
from location.serializers import GetLocationSerializer, PostLocationSerializer
# --state--
from location.serializers import GetStateSerializer, PostStateSerializer, GetFilteredStateSerializer,PatchStateSerializer
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.response import Response


#country api
class CountryApiView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin):

    @extend_schema(
        request=None,
        responses={200, GetCountrySerializer}
    )
    def get(self,request):
        queryset = Country.objects.all()
        serializer =GetCountrySerializer(queryset, many=True)
        if not serializer.is_valid:
            return serializer.errors
        return Response(serializer.data, status=status.HTTP_200_OK)



    @extend_schema(
        request=PostCountrySerializer,
        responses={200, GetCountrySerializer}
    )
    def post(self,request):
        serializer = PostCountrySerializer(data=request.data)
        if not serializer.is_valid():
            return serializer.errors
        country = Country(name=serializer.validated_data['name'])
        country.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)




class CountryFilteredApiView(generics.GenericAPIView,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin):
    @extend_schema(
        request=None,
        responses={200, CountrySerializer}
    )
    def get(self, request, *args, **kwargs):
        try:
            queryset = Country.objects.get(id=kwargs.get('id'))
        except:
            return Response("rakab khordi", status=status.HTTP_404_NOT_FOUND)
        context = {
            "name": queryset
        }
        output = CountrySerializer(context)
        return Response(data=output.data, status=status.HTTP_200_OK)




    @extend_schema(
        request=PostCountrySerializer,
        responses={200, GetCountrySerializer}
    )
    def patch(self, request, *args, **kwargs):
        try:
            record = Country.objects.get(id=kwargs.get('id'))
        except Country.DoesNotExist:
            return Response({'error': 'Country not found'}, status=404)

        serializer = PatchCountrySerializer(instance=record, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)


#-----------------------------------------------------------------------------------------------
#state api
class StateApiView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin):

    @extend_schema(
        request=None,
        responses={200, GetStateSerializer}
    )
    def get(self,request):
        queryset = State.objects.all()
        serializer =GetStateSerializer(queryset, many=True)
        if not serializer.is_valid:
            return serializer.errors
        return HttpResponse(serializer.data, content_type='application/json')



    @extend_schema(
        request=PostStateSerializer,
        responses={200, PostStateSerializer}
    )
    def post(self, request):
        serializer = PostStateSerializer(data=request.data)
        if not serializer.is_valid():
            return serializer.errors
        state = State(name=serializer.validated_data['name'])
        state.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)



class StateFilteredApiView(generics.GenericAPIView,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin):
    @extend_schema(
        request=None,
        responses={200, GetFilteredStateSerializer}
    )
    def get(self, request, *args, **kwargs):
        try:
            queryset = State.objects.get(id=kwargs.get('id'))
        except:
            return Response("rakab khordi", status=status.HTTP_404_NOT_FOUND)
        output = GetStateSerializer(queryset)
        return Response(data=output.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=PatchStateSerializer,
        responses={200, GetStateSerializer}
    )
    def patch(self, request, *args, **kwargs):
        try:
            record = Country.objects.get(id=kwargs.get('id'))
        except Country.DoesNotExist:
            return Response({'error': 'State not found'}, status=404)

        serializer = PatchCitySerializer(instance=record, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)


#----------------------------------------------------------------------------------------
#city api
class CityApiView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin):
    @extend_schema(
        request=None,
        responses={200, GetCitySerializer}
    )
    def get(self,request):
        queryset = City.objects.all()
        serializer =GetCitySerializer(queryset, many=True)
        if not serializer.is_valid:
            return serializer.errors
        return HttpResponse(serializer.data, content_type='application/json')

    @extend_schema(
        request=PostCitySerializer,
        responses={200, PostCitySerializer}
    )
    def post(self, request):
        serializer = PostCitySerializer(data=request.data)
        if not serializer.is_valid():
            return serializer.errors
        city = City(name=serializer.validated_data['name'])
        city.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)




class CityFilteredApiView(generics.GenericAPIView,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin):
    @extend_schema(
        request=None,
        responses={200, GetCitySerializer}
    )
    def get(self, request, *args, **kwargs):
        try:
            queryset = State.objects.get(id=kwargs.get('id'))
        except:
            return Response({"rakab": "khordi"}, status=status.HTTP_404_NOT_FOUND)
        context = {
            "name": queryset
        }
        output = GetCitySerializer(context)
        return Response(data=output.data, status=status.HTTP_200_OK)


    @extend_schema(
        request=PatchCitySerializer,
        responses={200, GetCitySerializer}
    )
    def patch(self, request, *args, **kwargs):
        try:
            record = Country.objects.get(id=kwargs.get('id'))
        except Country.DoesNotExist:
            return Response({'error': 'City not found'}, status=404)

        serializer = PatchCitySerializer(instance=record, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)

#----------------------------------------------------------------------------------
#location api
class LocationApiView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin):

    @extend_schema(
        request=None,
        responses={200, GetLocationSerializer}
    )
    def get(self,request):
        queryset = Location.objects.all()
        serializer =GetLocationSerializer(queryset, many=True)
        if not serializer.is_valid:
            return serializer.errors
        return HttpResponse(serializer.data, content_type='application/json')

    @extend_schema(
        request=PostLocationSerializer,
        responses={200, GetLocationSerializer}
    )
    def post(self,request):
        serializer = PostLocationSerializer(data=request.data)
        if not serializer.is_valid:
            return serializer.errors
        serializer.save()
        return Response(serializer.data, status=200)





class LocationFilteredApiView(generics.GenericAPIView,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin):
    def get(self,request,*args,**kwargs):
        queryset = Location.objects.filter(id= kwargs.get('id'))
        serializer = GetLocationSerializer(queryset, many=True)
        if not serializer.is_valid:
            return serializer.errors
        return HttpResponse(serializer.data, content_type='application/json')



