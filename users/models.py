from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, name, email, phone_number, password=None):
        if not username:
            raise ValueError('must have userid')
        if not name:
            raise ValueError('must have name')
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            username=username,
            name=name,
            email=self.normalize_email(email),
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password):
        user = self.create_user(
            username=username,
            name='admin',
            email=self.normalize_email(email),
            phone_number=phone_number,
            password=password
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=10, primary_key=True)  # cno
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True, )
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff


@property
def is_staff(self):
    return self.is_staff
