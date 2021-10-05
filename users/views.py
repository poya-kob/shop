from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        '''
         Instantiate the form with the submitted data with
         form = LoginForm(request.POST).
        '''
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Login Successfully!')
                    return redirect('/')
                else:
                    messages.error(request, 'Login Failed!')
            else:
                messages.error(request, ' Try again!')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # commit = FALSE -->> dont save in the database yet
            new_user.set_password(user_form.cleaned_data['password'])
            '''
             از set_password استفاده کردیم 
             برای اینکه میخوایم پسوورد رو هش کنه و همینجوری دخیره نکنه
            '''
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html', {'user_form': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def logout_page(request):
    logout(request)
    return redirect('/login/')


@login_required()
def dashboard(request):
    render(request, 'users/dashboard.html', {'section': 'dashboard'})


@login_required()
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.add_message(request, messages.SUCCESS, 'Your Profile Updated Successfully!')
            messages.success(request, 'Your Profile Updated Successfully!')
        else:
            messages.error(request, 'Profile Updating Failed!')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})
