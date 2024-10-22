from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User
from user.serializers import UserSerializer


#sign_in
class AuthenticationApiView(mixins.CreateModelMixin,
                            generics.GenericAPIView):

    @extend_schema(
        request=UserSerializer,
        responses= {200, UserSerializer}
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return serializer.errors
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# -------------------------------------------------------------------------------------------------------------
#sign_up
class RegistrationApiView(generics.GenericAPIView,
                           mixins.CreateModelMixin):

    @extend_schema(
        request=UserSerializer,
        responses={200, UserSerializer}
    )
    def post(self, request):
        serializer = UserSerializer(data= request.data)
        if not serializer.is_valid():
            return serializer.errors
        else:
            username= serializer.validated_data['username']
            if not User.objects.filter(username=username).exists():
                user = User(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
                user.save()
                return Response("successful registration", status= status.HTTP_200_OK)
            else:
                return Response("THis account already exist!", status= status.HTTP_400_BAD_REQUEST)

