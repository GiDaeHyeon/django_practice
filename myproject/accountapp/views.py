from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import HelloWorld2
from django.shortcuts import render

app_name = "accountapp"

# Create your views here.
def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld2()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse(f'{app_name}:hello_world'))
    else:
        hello_world_list = HelloWorld2.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy(f"{app_name}:hello_world")
    template_name = f'{app_name}/create.html'