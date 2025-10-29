from django.db import models

class Tache(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    dateAdd = models.DateTimeField(auto_now_add=True)
