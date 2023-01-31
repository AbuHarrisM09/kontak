from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dataperusahaan.models import Dataperusahaan
from datasiswa.models import Datasiswa
from datasekolah.models import Datasekolah
from .forms import RegisterForm


def signin(request):
    return render(request,'sign-in.html')

@login_required
def dashboard(request):
    total_siswa = Datasiswa.objects.all().count()
    total_perusahaan = Dataperusahaan.objects.all().count()
    total_sekolah = Datasekolah.objects.all().count()
    return render(request, 'dashboard.html', {'total_siswa': total_siswa, 'total_sekolah': total_sekolah, 'total_perusahaan': total_perusahaan})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'sign-up.html', {'form': form})

def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password']
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard/')

        else:
            form = AuthenticationForm()
        return render(request, 'sign-in.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('')

class ProtectedView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'next'

