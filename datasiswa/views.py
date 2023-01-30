from django.shortcuts import render, redirect
from .models import Datasiswa
from .forms import DatasiswaForm

# Create your views here.
def list_siswa(request):
    list = Datasiswa.objects.all()
    return render(request, 'siswa/list_siswa.html', {'list': list})

def create_siswa(request):
    if request.method == 'POST':
        form = DatasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/siswa')
    else:
        form = DatasiswaForm()
        return render(request,'siswa/create_siswa.html', {'form': form})