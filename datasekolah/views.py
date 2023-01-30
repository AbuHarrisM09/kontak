from django.shortcuts import render, redirect
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