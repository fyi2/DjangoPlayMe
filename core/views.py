# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import (
        UserCreationForm,
        UserChangeForm,
        PasswordChangeForm
        )
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect
from core.forms import ( EditAccountForm, SignUpForm,
                        ProfileForm,BankingForm
                        )
from core.models import UserProfile
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.

def peace(request):
    if request.method == 'POST':
        adjust = float(request.POST['betResult'])
        udata = UserProfile.objects.get(user=request.user)
        udata.user = request.user
        udata.betting_balance += adjust
        udata.save()
        args = {'form':request.POST}
        return render(request,'core/peace.html',args)
    else:
        print('Reloading War')
        return render(request,'core/war.html',{})

def snakedone(request):
    if request.method == 'POST':
        adjust = float(request.POST['betResult'])
        udata = UserProfile.objects.get(user=request.user)
        udata.user = request.user
        udata.betting_balance += adjust
        udata.save()
        args = {'form':request.POST}
        return render(request,'core/snakedone.html',args)
    else:
        print('Reloading War')
        return render(request,'core/snakeyes.html',{})


def view_profile(request):
    if request.method == 'POST':
        form = BankingForm(request.POST, instance=request.user.userprofile)
        udata = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            save_data = form.save(commit=False)
            save_data.user = request.user
            udata.user = request.user
            udata.bank_balance -= save_data.bank_balance
            udata.betting_balance += save_data.bank_balance
            udata.save()
            return redirect(reverse('core:profile'))
        return redirect(reverse('core:profile'))
    else:
        form = UserProfile.objects.get(user=request.user)
        args = {'form':form}
        return render(request,'core/profile.html',args)


def transfer(request):
    if request.method == 'POST':
        form = BankingForm(request.POST, instance=request.user.userprofile)
        udata = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            save_data = form.save(commit=False)
            save_data.user = request.user
            udata.user = request.user
            udata.bank_balance -= save_data.bank_balance
            udata.betting_balance += save_data.bank_balance
            udata.save()
            return redirect(reverse('core:profile'))
    else:
        udata = UserProfile.objects.get(user=request.user)
        form = BankingForm(instance=udata)
        args = {'form': form}
    return render(request, 'core/banking.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            save_data = form.save(commit=False)
            save_data.user = request.user
            save_data.save()
            return redirect(reverse('core:profile'))
    else:
        udata = UserProfile.objects.get(user=request.user)
        form = ProfileForm(instance=udata)
        args = {'form': form}
    return render(request, 'core/edit_profile.html', args)



def index(request):
    return render(request,"core/index.html", {})

def war(request):
    return render(request,"core/war.html", {})

def snakeyes(request):
    return render(request,"core/snakeyes.html", {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,"core/index.html", {})
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def edit_account(request):

    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request,"core/account.html", {})
    else:
        form = EditAccountForm(instance=request.user)
        args = {'form':form}
        return render(request,'core/edit_account.html', args)

def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request,"core/profile.html", {})
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'core/change_password.html', args)

def account(request):
    args = {'user':request.user}
    return render(request, 'core/account.html', args)
