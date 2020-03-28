from django.contrib import admin
from .models import *
from project.mixins import *

class PostAdmin(ViewOnSiteMixin, ViewImageMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'category',
                ('image', 'view_image'),
                'text',
                'updated',
            ],
            'classes': 'wide'
        }),
    ] + meta_data

    readonly_fields     = ['updated', 'view_image', 'view_image_a']
    list_display        = ['pk', 'title', 'view_image_a', 'on_site']
    list_display_links  = ['pk', 'title', 'view_image_a']
    list_select_related = ['category']
    view_on_site        = True


class PostCategoryAdmin(ViewOnSiteMixin, ViewImageMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'slug',
                ('image', 'view_image'),
                'updated',
            ],
            'classes': 'wide'
        }),
    ] + meta_data
    
    readonly_fields     = ['updated', 'view_image', 'view_image_a']
    list_display        = ['pk', 'title', 'view_image_a', 'on_site']
    list_display_links  = ['pk', 'title', 'view_image_a']
    view_on_site        = True


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
