from django.urls import path

from .views import list_sekolah

urlpatterns = [
    path("sekolah/", list_sekolah),
]