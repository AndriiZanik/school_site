from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ManyToManyField('Author',default='Admin')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photo = models.ImageField(blank=True,upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)

    def return_name_author(self):
        return self.author.get()

    def return_author_id(self):
        name = self.author.get()
        id = self.author.get(full_name=name)
        return id.pk

    def get_absolute_url(self):
        return reverse('news',kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']

class Author(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    position = models.CharField(default='',max_length=30)
    about_him = models.TextField(default=' ')
    photo_author = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')
    email = models.EmailField(default='email@gmail.com')
    phone_number = models.CharField(max_length=12,default='+380000000000')
    address = models.CharField(max_length=200,default='Ukraine')
    want_to_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


