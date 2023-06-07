from django.shortcuts import render, redirect


# Create your views here.
def reservation(request):
    return render(request, 'reservation/reserve.html')
