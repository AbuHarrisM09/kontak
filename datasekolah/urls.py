from django.urls import path

from .views import list_sekolah, create_sekolah

urlpatterns = [
    path("sekolah/", list_sekolah),
    path("sekolah/create-sekolah/", create_sekolah, name='create-sekolah'),
]