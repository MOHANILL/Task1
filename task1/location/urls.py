from django.urls import path
from location.views import CityApiView, CityFilteredApiView
from location.views import CountryApiView, CountryFilteredApiView
from location.views import LocationApiView, LocationFilteredApiView
from location.views import StateApiView, StateFilteredApiView


app_name = 'location'
urlpatterns =[
    path('country/', CountryApiView.as_view(), name='AllCountry'),
    path("country/<int:id>/", CountryFilteredApiView.as_view(), name="FilteredCountry"),

    path('state/', StateApiView.as_view(), name='AllState'),
    path("state/<int:id>/", StateFilteredApiView.as_view(), name="FilteredState"),

    path('city/', CityApiView.as_view(), name='AllCity'),
    path("city/<int:id>/", CityFilteredApiView.as_view(), name="FilteredCity"),

    path('location/', LocationApiView.as_view(), name='mp1'),
    path("location/<int:id>/", LocationFilteredApiView.as_view(), name="mp2"),

    ]