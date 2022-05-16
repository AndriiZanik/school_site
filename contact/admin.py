from django.contrib import admin
from .models import Responses

class ResponsesAdmin(admin.ModelAdmin):
    list_display = ['name','email','response']
    list_display_links = ['name','email']
    search_fields = ['name','email','response']


admin.site.register(Responses,ResponsesAdmin)

