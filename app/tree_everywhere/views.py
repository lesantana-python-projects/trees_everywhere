from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        data = {'user': request.user}
        return render(request, 'tree_everywhere/index.html', data)
