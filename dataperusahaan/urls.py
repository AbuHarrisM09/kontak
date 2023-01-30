from django.urls import path

from .views import list_perusahaan, create_perusahaan

urlpatterns = [
    path("perusahaan/", list_perusahaan),
    path("perusahaan/create-perusahaan/", create_perusahaan, name='create_perusahaan'),
]