from django.views.decorators.http import require_GET
from django.shortcuts import render

@require_GET
def robots_txt(request):
    return render(request, 'robots.html')