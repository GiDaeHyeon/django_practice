from django.views.generic.edit import DeleteView
from .forms import AccountUpdateForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import account_ownership_required

from .models import HelloWorld2
from django.shortcuts import render

app_name = "accountapp"
has_ownership = [account_ownership_required, login_required]

# Create your views here.
@login_required
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
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = f'{app_name}/detail.html'
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy(f"{app_name}:hello_world")
    template_name = f'{app_name}/update.html'
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy(f"{app_name}:login")
    template_name = f'{app_name}/delete.html'