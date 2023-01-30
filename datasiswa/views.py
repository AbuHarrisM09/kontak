from django.shortcuts import render, redirect, get_object_or_404
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

def edit_siswa(request, id):
    siswa = Datasiswa.objects.get(id=id)
    if request.method == 'POST':
        siswa.nama = request.POST['nama']
        siswa.email = request.POST['email']
        siswa.hp = request.POST['hp']
        siswa.alamat = request.POST['alamat']
        siswa.jenis_kelamin = request.POST['jenis_kelamin']
        siswa.tempat_lahir = request.POST['tempat_lahir']
        siswa.tanggal_lahir = request.POST['tanggal_lahir']
        siswa.nisn = request.POST['nisn']
        siswa.save()
        return redirect('index')
    return render(request, 'siswa/edit_siswa.html', {'siswa': siswa})

def delete_siswa(request, id):
    del_siswa = get_object_or_404(Datasiswa, id=id)
    del_siswa.delete()
    return redirect(request.META.get('HTTP_REFERER', '/siswa'))