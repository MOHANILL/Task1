from django.urls import path
from hall.views import HallApiView, HallFilteredApiView

app_name = 'hall'
urlpatterns =[
    path('hall/', HallApiView.as_view(), name='AllHall'),
    path("hall/<int:id>/", HallFilteredApiView.as_view(), name="FilteredHall"),
]