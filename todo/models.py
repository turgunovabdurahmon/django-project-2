from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatexd_at = models.DateTimeField(auto_now=True)



class Phone(models.Model):
    name = models.CharField(max_length=999, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    price = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatexd_at = models.DateTimeField(auto_now=True)


class Talaba(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    familiya = models.TextField(blank=True, null=True)
    telefon_nomer = models.CharField(max_length=225, unique=True)
    email = models.TextField(unique=True)
    biografiya = models.CharField(blank=True, null=True)
    yosh = models.TextField(default=0)
    kurs = models.CharField(max_length=15,choices=[
        ("1-course","1-course"),
        ("2-course","2-course"),
        ("3-course","3-course"),
        ("4-course","4-course"),
    ])
    rasm = models.ImageField()
    tugallaganmi = models.BooleanField(default=False)
    tugilgan_kun = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

