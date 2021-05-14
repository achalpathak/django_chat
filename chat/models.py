from django.db import models

# Create your models here.


class Agents(models.Model):
    username = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.username


class Customers(models.Model):
    username = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.username


class Messages(models.Model):
    username = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_added",)
