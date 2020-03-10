from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['updated']

class PostCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['updated']

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)


