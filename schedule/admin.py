from django.contrib import admin

from schedule.models import Classes, DayOfWeak,Subjects


class ClassesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount_students']
    list_display_links = ['id', 'name']
    # search_fields = ['title','content']


class DayOfWeakAdmin(admin.ModelAdmin):
    list_display = ['day']


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']


admin.site.register(Classes, ClassesAdmin)
admin.site.register(DayOfWeak, DayOfWeakAdmin)
admin.site.register(Subjects, SubjectsAdmin)
