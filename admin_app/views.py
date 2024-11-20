from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# Create your views here.
def login_required_decorator(func):
    return login_required(function=func, login_url='login-page')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login-page')
    template_name = 'signup.html'


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            return redirect('home-page')

    return render(request, template_name='login.html')


@login_required_decorator
def logout_page(reqeust):
    logout(request=reqeust)

    return redirect('login-page')


@login_required_decorator
def home_page(reqeust):
    return render(request=reqeust, template_name='index.html')
