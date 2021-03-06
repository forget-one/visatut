from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

class VacancyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name']
        }),
        ('Параметри пошуку', {
            'classes': ('extrapretty', 'wide',),
            'fields': [('country', 'gender', 'document', 'work_type'),]
        }),
        ('Основна інформація', {
            'fields': ['requirements', 'work_position', 'work_day' , 'your_duties', 'our_duties', 'duties', 'actual',]
        })
    )

    list_filter = ['actual']
    list_display = ['pk', 'name', 'country', 'actual']
    list_display_links = ['pk', 'name', 'country', 'actual']

class GenderAdmin(admin.ModelAdmin):
    exclude = ['']

class DocumetTypeAdmin(admin.ModelAdmin):
    exclude = ['']

class WorkTypeAdmin(admin.ModelAdmin):
    exclude = ['']
    


class CountryNameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
            ],
            'classes': 'wide'
        }),
    ]
    list_display        = ['id', 'title']
    list_display_links  = ['id', 'title']
    

admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(DocumetType, DocumetTypeAdmin)
admin.site.register(CountryName, CountryNameAdmin)