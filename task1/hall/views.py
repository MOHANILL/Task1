from drf_spectacular.utils import extend_schema
from hall.models import Hall
from hall.serializers import GetHallSerializer, PostHallserializer, PatchHallSerializer
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.response import Response


class HallApiView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin):

    @extend_schema(
        request=None,
        responses={200, GetHallSerializer}
    )
    def get(self,request):
        queryset = Hall.objects.all()
        serializer =GetHallSerializer(queryset, many=True)
        if not serializer.is_valid:
            return serializer.errors
        return Response(serializer.data, status=status.HTTP_200_OK)



    @extend_schema(
        request=PostHallserializer,
        responses={200, GetHallSerializer}
    )
    def post(self,request):
        serializer = PostHallserializer(data=request.data)
        if not serializer.is_valid():
            return serializer.errors
        hall = Hall(name=serializer.validated_data['name'], capacity= serializer.validated_data['capacity'])
        hall.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)





class HallFilteredApiView(generics.GenericAPIView,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin):
    @extend_schema(
        request=None,
        responses={200, GetHallSerializer}
    )
    def get(self, request, *args, **kwargs):
        try:
            queryset = Hall.objects.get(id=kwargs.get('id'))
        except:
            return Response("rakab khordi", status=status.HTTP_404_NOT_FOUND)

        output = GetHallSerializer(queryset)
        return Response(data=output.data, status=status.HTTP_200_OK)


    @extend_schema(
            request=PatchHallSerializer,
            responses={200, GetHallSerializer}
        )
    def patch(self, request, *args, **kwargs):
        try:
            record = Hall.objects.get(id=kwargs.get('id'))
        except Hall.DoesNotExist:
            return Response({'error': 'Country not found'}, status=404)

        serializer = PatchHallSerializer(instance=record, data=request.data, partial=True)

        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)





