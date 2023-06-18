from django import forms
from rentcar.models import RentCar


class ReservationForm(forms.ModelForm):
    class Meta:
        model = RentCar
        fields = ['dateRented', 'dateDue']
