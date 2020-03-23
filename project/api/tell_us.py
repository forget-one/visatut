from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail

@csrf_exempt
def tell_us(request):
    data = request.POST 
    send_mail(
        f"Sps za babki {data.get('name')}, {data.get('phone')}, {data.get('email')}",
        'you are welcome',
        settings.EMAIL_HOST_USER,
        ['easyebengrad@gmail.com'],
        fail_silently=False
    )
    return JsonResponse({'status': 'OK'})