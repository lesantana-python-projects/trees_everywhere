from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from app.tree_everywhere.models import PlantedTree


class PlantTreeCreate(LoginRequiredMixin, CreateView):
    model = PlantedTree
    fields = ['age', 'tree', 'latitude', 'longitude']
    template_name = 'tree_everywhere/to_plant.html'

    def form_valid(self, form):
        tree = form.save(commit=False)
        tree.user_id = self.request.user.id
        tree.account_id = self.request.session['account_id']
        tree.save()
        return redirect(reverse('tree_everywhere_home'))
