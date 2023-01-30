from django.urls import path

from .views import list_siswa, create_siswa

urlpatterns = [
    path("siswa/", list_siswa),
    path("siswa/create-siswa/", create_siswa, name='create-siswa'),
]