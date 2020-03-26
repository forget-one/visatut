from django.contrib import admin
from .models import *
from project.mixins import *

class PostInline(ViewImageMixin, admin.StackedInline):
    model       = Post
    extra       = 0
    fieldsets   = [
        (None, {
            'fields': [
                'title',
                ('image', 'view_image'),
                'text',
                'updated',
            ],
            'classes': ['wide'],
        }),
    ] + meta_data

    readonly_fields = ['updated', 'view_image']

class PostAdmin(ViewOnSiteMixin, ViewImageMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'post_category',
                ('image', 'view_image'),
                'text',
                'updated',
            ],
            'classes': 'wide'
        }),
    ] + meta_data

    readonly_fields     = ['updated', 'view_image']
    list_display        = ['pk', 'title', 'view_image', 'on_site',]
    list_display_links  = ['pk', 'title',]
    list_select_related = ['post_category']
    view_on_site        = True


class PostCategoryAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'slug',
                'updated',
            ],
            'classes': 'wide'
        }),
    ] + meta_data
    save_as = True  
    readonly_fields     = ['updated',]
    inlines             = [PostInline]
    list_display        = ['pk', 'title', 'on_site']
    list_display_links  = ['pk', 'title',]
    view_on_site        = True

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)


