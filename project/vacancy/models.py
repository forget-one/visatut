from django.db import models

# Create your models here.

class Vacancy(models.Model):
    country         = models.ForeignKey(to='services.Country', on_delete=models.CASCADE, blank=True, null=True)
    category        = models.ManyToManyField(to='Gender', blank=True, related_name='vacancies')
    document        = models.ForeignKey(to='DocumetType', blank=True, on_delete=models.CASCADE, null=True, related_name='documents')
    requirements    = models.TextField(blank=True, null=True)
    work_position   = models.CharField(max_length=1000, blank=True, null=True)
    work_day        = models.CharField(max_length=1000, blank=True, null=True)
    our_duties      = models.TextField(blank=True, null=True)
    duties          = models.TextField(blank=True, null=True)

    
class Gender(models.Model):
    human_type = models.CharField(max_length=100, blank=True, null=True)
    
class DocumetType(models.Model):
    doc_type    = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)