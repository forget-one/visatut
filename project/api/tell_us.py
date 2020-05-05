from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail

@csrf_exempt
def tell_us(request):
    data = request.POST
    send_mail(
        f"{data.get('name')}, {data.get('phone')}, {data.get('email')}",
        f"Name: {data.get('name')}, Phone: {data.get('phone')}, Email: {data.get('email')}",
        settings.EMAIL_HOST_USER,
        ['easyebengrad@gmail.com'],
        fail_silently=False
    )
    return JsonResponse({'status': 'OK'})