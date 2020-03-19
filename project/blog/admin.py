from django.contrib import admin
from .models import *
from project.mixins import *

class PostInline(admin.StackedInline):
    model       = Post
    extra       = 0
    fieldsets   = [
        (None, {
            'fields': [
                'title',
                ('image', 'img_alt'),
                'text',
                'updated',
            ],
            'classes': ['wide'],
        }),
        ('Мета-дані', {
            'fields': [
                'meta_title',
                'meta_descr',
                'meta_key',
            ],
            'classes': ['collapse']
        }),
    ]
    readonly_fields = ['updated',]

class PostAdmin(ViewOnSiteMixin, ViewImage, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'post_category',
                ('image', 'img_alt'),
                'view_image',
                'text',
                'updated',
            ],
            'classes': 'wide'
        }),
        ('Мета-дані', {
            'fields': [
                'meta_title',
                'meta_descr',
                'meta_key',
            ],
            'classes': ['collapse']
        }),
    ]
    readonly_fields     = ['updated', 'view_image']
    list_display        = ['pk', 'title', 'view_image', 'on_site',]
    list_display_links  = ['pk', 'title',]
    list_select_related = ['post_category']
    view_on_site        = True


class PostCategoryAdmin(ViewOnSiteMixin, ViewImage, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'slug',
                ('image', 'img_alt'),
                'text',
                'updated',
            ],
            'classes': 'wide'
        }),
        ('Мета-дані', {
            'fields': [
                'meta_title',
                'meta_descr',
                'meta_key',
            ],
            'classes': ['collapse']
        }),
    ]
    readonly_fields     = ['updated',]
    inlines             = [PostInline]
    list_display        = ['pk', 'title', 'on_site']
    list_display_links  = ['pk', 'title',]
    view_on_site        = True

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)


