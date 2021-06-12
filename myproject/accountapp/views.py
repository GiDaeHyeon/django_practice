from django.shortcuts import render

appname = "accountapp"

# Create your views here.
def hello_world(request):
    return render(request, 'base.html')