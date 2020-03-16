from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'post_category',
                ('image', 'img_alt'),
                'text',
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
        (None, {
            'fields': [
                'updated',
            ]
        })
    ]
    readonly_fields = ['updated']
    list_per_page = 30


class PostCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'slug',
                ('image', 'img_alt'),
                'text',
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
        (None, {
            'fields': [
                'updated',
            ]
        })
    ]
    readonly_fields = ['updated']

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)


