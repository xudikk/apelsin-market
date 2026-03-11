from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(
            username=username,
            password=password,
            **extra_fields
        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(verbose_name="To'lliq Ism Familiya", max_length=56)
    username = models.CharField("Foydalanuvchi Nomi", unique=True, max_length=56)
    age = models.SmallIntegerField(default=18, verbose_name="Yoshi")
    gender = models.BooleanField(choices=[
        (True, "Erkak"),
        (False, "Ayol"),
    ], default=True, verbose_name="Jinsi")

    role = models.SmallIntegerField(choices=[
        (1, "Admin"),
        (2, "Seller"),
        (3, "Buyer"),
    ], default=3, help_text="Admin(1), Seller(2), Buyer(3)")

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["role"]


class Firma(models.Model):
    name = models.CharField("Online magazin nomi", max_length=56)
    logo = models.ImageField(upload_to="brands/", null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={
        "role": 2
    })








