from django.contrib import admin
from info.models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name',
                    'age', 'position', 'about_him', 'education', 'experience']
    list_display_links = ['id','first_name', 'last_name']
    search_fields = ['first_name', 'last_name','position', 'education', 'experience']


admin.site.register(Teacher,TeacherAdmin)
