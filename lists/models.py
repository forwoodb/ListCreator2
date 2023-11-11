from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ListName(models.Model):
    list_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.list_name


class ListItem(models.Model):
    list_n = models.ForeignKey(ListName, on_delete=models.CASCADE, null=True)
    list_item = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.list_item
