from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from rentcar.models import *
from users.models import User
from django.db.models import Count


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def history(request):
    current = RentCar.objects.filter(cno__username=request.user.username)
    prev = PreviousRental.objects.filter(cno__username=request.user.username)
    context = {
        'current': current,
        'prev': prev,
    }
    return render(request, 'users/history.html', context)


def admin(request):
    car = CarModel.objects.all()
    current = RentCar.objects.all()
    prev = PreviousRental.objects.all()
    user = User.objects.all()
    #group = CarModel.objects.values('modelName', 'vehicleType').annotate(total=Count('modelName'), first='')
    context = {
        'current': current,
        'prev': prev,
        'user': user,

    }
    return render(request, 'users/admin.html', context)
