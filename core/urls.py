
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('tinymce/', include('tinymce.urls')),
]


if settings.DEBUG == True:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



def test_mail(request):
  from django.core.mail import send_mail 
  print(settings.EMAIL_HOST_USER)
  send_mail(
    'hello',
    'world',
    settings.EMAIL_HOST_USER,
    ['easyebengrad@gmail.com'],
    # fail_silently=True
    fail_silently=False
  )
  from django.http import HttpResponse
  return HttpResponse('ok')

urlpatterns += [
  path('test_mail/', test_mail, name='test_mail'),

]