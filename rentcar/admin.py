from django.contrib import admin
from .models import CarModel, RentCar, Reserve, PreviousRental, Options

# Register your models here.

admin.site.register(CarModel)
admin.site.register(RentCar)
admin.site.register(Reserve)
admin.site.register(PreviousRental)
admin.site.register(Options)
