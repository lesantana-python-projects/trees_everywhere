from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.tree_everywhere.models import Tree


class TreeList(LoginRequiredMixin, ListView):
    model = Tree
    fields = ['name', 'scientific_name']
    template_name = 'tree_everywhere/trees.html'
