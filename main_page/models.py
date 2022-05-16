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
        if type(self.author.get()) == 'class':
            #return type(self.author.get())
            return self.author.get()
        return 'Admin'


    def get_absolure_url(self):
        return reverse('news',kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']

class Author(models.Model):
    full_name = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


