from django.urls import path
from . import views


app_name = 'rentcar'

urlpatterns = [
    path('', views.home, name='home'),
]
