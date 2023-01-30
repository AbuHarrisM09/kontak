from django.urls import path

from .views import list_siswa, create_siswa, edit_siswa, delete_siswa

urlpatterns = [
    path("siswa/", list_siswa),
    path("siswa/create-siswa/", create_siswa, name='create-siswa'),
    path("siswa/edit/<int:id>/", edit_siswa, name='/siswa/edit'),
    path("siswa/delete/<int:id>/", delete_siswa, name='/siswa/delete'),
]