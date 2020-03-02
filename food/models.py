from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
  item_name = models.CharField(max_length = 200)
  item_desc = models.CharField(max_length = 200)
  item_price = models.IntegerField()
  item_image = models.CharField(max_length = 500, default = 'https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg')

  def __str__(self):
    return self.item_name
  

  def get_absolute_url(self):
    return reverse('food:detail', kwargs = { 'pk': self.pk })
