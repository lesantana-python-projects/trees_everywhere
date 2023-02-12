from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from app.account.forms import LoginForm


class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'account/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

        data = {
            'form': form,
            'error': 'User not found'
        }
        return render(request, 'account/login.html', data)
