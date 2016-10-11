from django.shortcuts import render
from django.http import HttpResponse

firstResponse = "Polls index <a href='https://docs.djangoproject.com/en/1.10/intro/tutorial01/'>Tutorial</a> seite.<br>to be continued"

def index(request):
    return HttpResponse(firstResponse)
