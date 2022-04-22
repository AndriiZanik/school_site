from django.contrib import admin

from .models import News
from .models import Author

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at','is_published']
    list_display_links = ['id','title']
    search_fields = ['title','content']


admin.site.register(News,NewsAdmin)

class AuthorAdmin(admin.ModelAdmin):
     list_display = ['full_name']

admin.site.register(Author,AuthorAdmin)