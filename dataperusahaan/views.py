from django.shortcuts import render
from .models import Dataperusahaan

# Create your views here.
def list_perusahaan(request):
    list = Dataperusahaan.objects.all()
    return render(request, 'list_perusahaan.html', {'list': list})