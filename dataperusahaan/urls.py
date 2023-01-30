from django.urls import path
from .views import list_perusahaan, create_perusahaan, edit_perusahaan, delete_perusahaan

urlpatterns = [
    path("perusahaan/", list_perusahaan),
    path("perusahaan/create-perusahaan/", create_perusahaan, name='create_perusahaan'),
    path("perusahaan/edit/<int:id>/", edit_perusahaan, name='/perusahaan/edit'),
    path("perusahaan/delete/<int:id>/", delete_perusahaan, name='/perusahaan/delete'),
]