from django.contrib.auth.models import User
from django.db import models
from rest_framework.serializers import ModelSerializer
# from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     custom_field = models.CharField(
#         verbose_name='Some custom field', max_length=250)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfile(models.Model):
    custom_field = models.CharField(
        verbose_name='Some custom field', max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
