from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.views.generic import FormView

from .forms import LoginForm, UserRegistrationForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'myshop/list.html')
                else:
                    return HttpResponse('Konto zablokowane')
            else:
                return HttpResponse('Złe dane')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return render(request, 'myshop/list.html')


class Register(FormView):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/login.html')
        else:
            form = UserRegistrationForm()
        return render(request, 'account/register.html', {'form':form})






