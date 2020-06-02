from django.views.decorators.http import require_GET
from django.shortcuts import render

@require_GET
def robots_txt(request):
    return render(request, 'robots.html')

def view_400(request, exception):
    return render(request, 'exceptions/400.html')

def view_403(request, exception):
    return render(request, 'exceptions/403.html')

def view_404(request, exception):
    return render(request, 'exceptions/404.html')

def view_500(request, exception):
    return render(request, 'exceptions/500.html')