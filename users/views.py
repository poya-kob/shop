from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from .forms import LoginForm, UserRegistrationForm
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
                    return HttpResponse('Authenticate successfully')
                else:
                    messages.error(request, 'Login Failed!')
                    return HttpResponse('Disable account')
            else:
                messages.error(request, ' Try again!')
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


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
            return render(request, 'users/login.html', {'user_form': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})
