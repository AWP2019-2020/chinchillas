from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    price = models.FloatField()
    rating = models.FloatField()
    image = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name']
