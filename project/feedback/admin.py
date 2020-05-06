from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.
class SupportAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      "fields": (
        ('name', 'phone', 'email'),
        'added',
        'finished'
      ),
      'classes': 'wide'
    }),
  )
  def on_site(self, obj):
    clear_phone = ''
    if obj.phone:
      clear_phone = obj.phone.replace(' ', '').replace('(', '').replace(')', '')
    return mark_safe(f"<a href='tel:{clear_phone}'>{obj.phone}</a>")
  on_site.short_description = "Зателефонувати"

  readonly_fields     = ['added']
  list_editable       = ['finished']
  list_display        = ['pk', 'name', 'on_site', 'email', 'finished']
  list_display_links  = ['pk', 'name', 'email']
  
admin.site.register(Support, SupportAdmin)