from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    topic=input('enter topic-name:')
    TO=Topic.objects.get_or_create(Topic_name=topic)[0]
    TO.save()
    return HttpResponse('topic is inserted')
def insert_webpage(request):
    topic=input('enter topic-name:')
    TO=Topic.objects.get_or_create(Topic_name=topic)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=WebPage.objects.get_or_create(Topic_name=TO,Name=n,Url=u)[0]
    WO.save()
    return HttpResponse(' webpage topic is inserted')
def insert_access(request):
    topic=input('enter topic-name:')
    TO=Topic.objects.get_or_create(Topic_name=topic)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=WebPage.objects.get_or_create(Topic_name=TO,Name=n,Url=u)[0]
    WO.save()
    D=input('enter date:')
    A=input('enter author:')
    ARO=AccessRecords.objects.get_or_create(Name=WO,Date=D,Author=A)[0]
    ARO.save()
    return HttpResponse(' access topic is inserted')
