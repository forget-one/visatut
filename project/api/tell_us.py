from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from project.feedback.models import *
from django.urls import reverse
from django.template.loader import render_to_string

@csrf_exempt
def tell_us(request):
    data    = request.POST
    name    = data.get('name')
    phone   = data.get('phone')
    email   = data.get('email')
    client  = Support.objects.create(
        name    = name,
        phone   = phone,
        email   = email,
    )
    admin_url   = 'https://visatut.in.ua' + reverse(f'admin:{client._meta.app_label}_{client._meta.model_name}_change', args=(client.pk,))
    context = {
        'admin_url': admin_url,
        'name': name,
        'phone': phone,
        'email': email
    }
    link = render_to_string('tell_us.html', context)
    send_mail(
    f"{name}, {phone}",
    link,
    settings.EMAIL_HOST_USER,
    ['easyebengrad@gmail.com'],
    fail_silently=False
    )
    return JsonResponse({'status': 'OK'})
