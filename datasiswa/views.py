from django.shortcuts import render
from .models import Datasiswa

# Create your views here.
def list_siswa(request):
    list = Datasiswa.objects.all()
    return render(request, 'list_siswa.html', {'list': list})