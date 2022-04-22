from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ManyToManyField('Author',default='Admin')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photo = models.ImageField(blank=True,upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)

    def return_name_author(self):
        return self.author.all().__str__()

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']

class Author(models.Model):
    full_name = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


