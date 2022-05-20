from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News
from .models import Author

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at','is_published','get_photo']
    list_display_links = ['id','title']
    search_fields = ['title','content']
    # fields = ['id','title','is_published']
    # readonly_fields = ['get_photo']

    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img srk="{obj.photo.url}" width="50">')
        return 'No photo'


admin.site.register(News,NewsAdmin)

class AuthorAdmin(admin.ModelAdmin):
     list_display = ['full_name']

admin.site.register(Author,AuthorAdmin)