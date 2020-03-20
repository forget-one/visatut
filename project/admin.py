from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

class PageAdmin(admin.ModelAdmin):
    exclude = ['']

admin.site.register(Page, PageAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)


admin.site.site_header  = 'Visatut адміністрування'
admin.site.site_title   = 'Visatut адміністрування'
admin.site.index_title  = ''

