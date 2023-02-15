from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import (authenticate, login, logout)
from app.account.forms import LoginForm


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'account/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            account = form.cleaned_data.get('account')

            user = authenticate(username=username, password=password)
            if user and account.users.filter(id=user.id).count():
                login(request, user)
                request.session['account_id'] = account.id
                return HttpResponseRedirect(reverse('tree_everywhere_home'))

        data = {
            'form': form,
            'error': 'User not found'
        }
        return render(request, 'account/login.html', data)
