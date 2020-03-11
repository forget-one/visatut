from django.contrib import admin
from .models import *


class PageAdmin(admin.ModelAdmin):
    exclude = ['']

admin.site.register(Page, PageAdmin)