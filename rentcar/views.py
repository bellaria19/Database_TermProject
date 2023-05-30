from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def home(request):
    #page = request.GET.get('page', '1')  # 페이지
    return render(request, 'rentcar/home.html')
