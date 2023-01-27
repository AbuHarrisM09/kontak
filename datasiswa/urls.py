from django.urls import path

from .views import list_siswa

urlpatterns = [
    path("siswa/", list_siswa),
]