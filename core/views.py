from django.views.decorators.http import require_GET
from django.shortcuts import render
from django.http import Http404
from django.views.defaults import (
    bad_request, permission_denied, page_not_found, server_error
)

@require_GET
def robots_txt(request):
    return render(request, 'robots.html')

def view_400(request, exception):
    return bad_request(request, exception, 'exceptions/400.html')

def view_403(request, exception):
    return permission_denied(request, exception, 'exceptions/403.html')

def view_404(request, exception):
    return page_not_found(request, exception, 'exceptions/404.html')

def view_500(request):
    return server_error(request, 'exceptions/500.html')