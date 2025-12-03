from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatexd_at = models.DateTimeField(auto_now=True)
    

