from django.contrib import admin
from .models import *
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


class GenderAdmin(admin.ModelAdmin):
    exclude = ['']


class DocumetTypeAdmin(admin.ModelAdmin):
    exclude = ['']


class WorkTypeAdmin(admin.ModelAdmin):
    exclude = ['']

admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(DocumetType, DocumetTypeAdmin)