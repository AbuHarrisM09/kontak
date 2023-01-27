from django.urls import path

from .views import list_perusahaan

urlpatterns = [
    path("perusahaan/", list_perusahaan),
]