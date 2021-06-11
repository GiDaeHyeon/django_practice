from django.http.response import HttpResponse
from django.shortcuts import render

appname = "accountapp"

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!!")