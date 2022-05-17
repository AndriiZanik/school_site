from django.db import models
from django.urls import reverse

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=1)
    position = models.CharField(default='', max_length=30)
    about_him = models.TextField(default=' ')
    education = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')

    def get_absolute_url(self):
        return reverse('news',kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        #ordering = ['-created_at']
