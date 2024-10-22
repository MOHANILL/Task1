from django.urls import path
from user.views import AuthenticationApiView
from user.views import RegistrationApiView


app_name= 'user'
urlpatterns = [
    path('login/', AuthenticationApiView.as_view(), name='login'),
    path('sign-up/', RegistrationApiView.as_view(), name='sign-up')

]