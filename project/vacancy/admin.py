from django.contrib import admin
from .models import *
# Register your models here.

class VacancyAdmin(admin.ModelAdmin):
    exclude = ['']


class GenderAdmin(admin.ModelAdmin):
    exclude = ['']


class DocumetTypeAdmin(admin.ModelAdmin):
    exclude = ['']

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(DocumetType, DocumetTypeAdmin)