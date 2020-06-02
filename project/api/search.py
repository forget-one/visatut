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
    vacancies = vacancies.objects.all()
    country__title      = data.get('vant1')
    gender__human_type  = data.get('vant2')
    work_type__work_type= data.get('vant3')
    document__doc_type  = data.get('vant4')
    actual              = vant5(data.get('actual'))
    if country__title: vacancies.filter(country__title=country__title)
    if gender__human_type: vacancies.filter(gender__human_type=gender__human_type)
    if work_type__work_type: vacancies.filter(work_type__work_type=work_type__work_type)
    if document__doc_type: vacancies.filter(document__doc_type=document__doc_type)
    if actual: vacancies.filter(actual=actual)
    page, created = Page.objects.get_or_create(
        slug    = f"{request.build_absolute_uri()}")
    return render(request, 'search_service.html', {
        'vacancies': vacancies,
    })
    