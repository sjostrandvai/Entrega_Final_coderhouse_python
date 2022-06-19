from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Avatars(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)