from django.urls import path
from .views import ContainerIdView

urlpatterns = [
    path('container-id/', ContainerIdView.as_view(), name='container-id'),
]