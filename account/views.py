from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.views import View
from django.views.generic import FormView

from .forms import LoginForm, UserRegistrationForm, UserEditForm, UserProfileForm


# Create your views here.
from .models import ProfileUser


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        errors = 'złe dane'
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'myshop/list.html')
            else:
                return render(request, 'account/login.html', {'errors':errors})
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
            ProfileUser.objects.create(user=new_user)
            return render(request, 'myshop/list.html')
        else:
            form = UserRegistrationForm()
        return render(request, 'account/register.html', {'form':form})



@login_required
def user_detail(request):
    return render(request, 'account/user.html')



@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = UserProfileForm(instance=request.user.profileuser,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profileuser)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})

