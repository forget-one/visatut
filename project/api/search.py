from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from project.vacancy.models import *
from project.models import Page


@csrf_exempt
def search_service(request):
    data = request.POST
    def vant5(value):
        if value == 'True': return True
        return False 
    vacancies = Vacancy.objects.filter(
        country__title      = data.get('vant1'),
        gender__human_type  = data.get('vant2'),
        work_type__work_type= data.get('vant3'),
        document__doc_type  = data.get('vant4'),
        actual              = vant5(data.get('actual'))
    ).select_related('country', 'gender', 'document', 'work_type',)
    page, created = Page.objects.get_or_create(
        slug    = f"{request.build_absolute_uri()}")
    return render(request, 'search_service.html', locals())
    