from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

from app.account.models import UserAccount
from app.tree_everywhere.models import PlantedTree
from django.db.models import Q


class PlantTreeCreate(LoginRequiredMixin, CreateView):
    model = PlantedTree
    fields = ['age', 'tree', 'latitude', 'longitude']
    template_name = 'tree_everywhere/to_plant.html'

    def form_valid(self, form):
        tree = form.save(commit=False)
        tree.user_id = self.request.user.id
        tree.account_id = self.request.session['account_id']
        tree.save()
        return redirect(reverse('tree_everywhere_planted'))


class PlantTreeList(LoginRequiredMixin, ListView):
    model = PlantedTree
    fields = ['age', 'tree', 'latitude', 'longitude']
    template_name = 'tree_everywhere/planted_trees.html'

    def get_queryset(self):
        user_id = self.request.user.id
        account_belongs_ids = list(UserAccount.objects.filter(user=user_id).values_list('account_id', flat=True))
        queryset = PlantedTree.objects.filter(Q(user__id=user_id) | Q(account_id__in=account_belongs_ids))
        return queryset
