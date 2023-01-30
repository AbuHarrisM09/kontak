from django.urls import path

from .views import list_sekolah, create_sekolah, edit_sekolah, delete_sekolah

urlpatterns = [
    path("sekolah/", list_sekolah),
    path("sekolah/create-sekolah/", create_sekolah, name='create-sekolah'),
    path("sekolah/edit/<int:id>", edit_sekolah, name='/sekolah/edit'),
    path("sekolah/delete/<int:id>", delete_sekolah, name='/sekolah/delete'),
]