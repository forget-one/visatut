from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from project.vacancy.models import *
from project.models import Page


@csrf_exempt
def search_service(request):
    data = request.GET
    def vant5(value):
        if value == 'True': return True
        return False 
    vacancies   = Vacancy.objects.all()
    country     = data.get('vant1')
    gender      = data.get('vant2')
    work_type   = data.get('vant3')
    document    = data.get('vant4')
    actual      = vant5(data.get('actual'))
    print(data, 'data')
    if country != '0': vacancies = vacancies.filter(country__title=country)
    if gender != '0': vacancies = vacancies.filter(gender__human_type=gender)
    if work_type != '0': vacancies = vacancies.filter(work_type__work_type=work_type)
    if document != '0': vacancies = vacancies.filter(document__doc_type=document)
    vacancies = vacancies.filter(actual=actual)
    page, created = Page.objects.get_or_create(
        slug    = f"{request.build_absolute_uri()}")
    return render(request, 'search_service.html', {'vacancies': vacancies,})
    