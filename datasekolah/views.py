from django.shortcuts import render, redirect, get_object_or_404
from .models import Datasekolah
from .forms import DatasekolahForm

# Create your views here.
def list_sekolah(request):
    list = Datasekolah.objects.all()
    return render(request, 'sekolah/list_sekolah.html', {'list': list})

def create_sekolah(request):
    if request.method == 'POST':
        form = DatasekolahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sekolah')
    else:
        form = DatasekolahForm()
        return render(request, 'sekolah/create_sekolah.html', {'form': form})
    
def edit_sekolah(request, id):
    sekolah = Datasekolah.objects.get(id=id)
    if request.method == 'POST':
        sekolah.npsn = request.POST['npsn']
        sekolah.nama = request.POST['nama']
        sekolah.email = request.POST['email']
        sekolah.hp = request.POST['hp']
        sekolah.alamat = request.POST['alamat']
        sekolah.provinsi = request.POST['provinsi']
        sekolah.kabupaten_kota = request.POST['kabupaten_kota']
        sekolah.kecamatan = request.POST['kecamatan']
        sekolah.status = request.POST['status']
        return redirect('index')
    return render(request, 'sekolah/edit_sekolah.html', {'sekolah':sekolah})

def delete_sekolah(request, id):
    del_sekolah = get_object_or_404(Datasekolah, id=id)
    del_sekolah.delete()
    return redirect(request.META.get('HTTP_REFERER', '/perusahaan'))