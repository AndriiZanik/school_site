from django.db import models


class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photo = models.ImageField(blank=True,upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
