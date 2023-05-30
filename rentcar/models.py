from django.db import models


# Create your models here.
class CarModel(models.Model):
    modelName = models.CharField(max_length=100, primary_key=True)
    vehicleType = models.CharField(max_length=100)
    rentRatePerDay = models.IntegerField()
    fuel = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()


# class User(models.Model):
#    cno = models.CharField(max_length=10, primary_key=True)  # 아이디
#    name = models.CharField(max_length=100)
#    passwd = models.CharField(max_length=100)
#    email = models.CharField(max_length=150)

class RentCar(models.Model):
    licensePlateNo = models.CharField(max_length=20, primary_key=True)
    modelName = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    dateRented = models.DateField(blank=True, null=True)
    dateDue = models.DateField(blank=True, null=True)
    cno = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True)


# primary_key = PlateNo, startDate
class Reserve(models.Model):
    licensePlateNo = models.ForeignKey(RentCar, on_delete=models.CASCADE)
    startDate = models.DateField()
    reserveDate = models.DateField()
    endDate = models.DateField()
    cno = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['licensePlateNo', 'startDate'], name='unique_licensePlateNo_startDate_combination'
            )
        ]


# primary_key = PlateNo, dateRented
class PreviousRental(models.Model):
    licensePlateNo = models.ForeignKey(RentCar, on_delete=models.CASCADE)
    dateRented = models.DateField()
    dateReturned = models.DateField()
    payment = models.IntegerField()
    cno = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['licensePlateNo', 'dateRented'], name='unique_licensePlateNo_dateRented_combination'
            )
        ]


class Options(models.Model):
    licensePlateNo = models.ForeignKey(RentCar, on_delete=models.CASCADE)
    optionName = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['licensePlateNo', 'optionName'], name='unique_licensePlateNo_optionName_combination'
            )
        ]
