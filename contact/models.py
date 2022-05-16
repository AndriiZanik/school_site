from django.db import models

class Responses(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    response = models.TextField()
