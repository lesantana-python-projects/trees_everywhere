from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views import View

from app.tree_everywhere.models import PlantedTree


class ApiTreesPlantedByUser(LoginRequiredMixin, View):
    def get(self, request):
        trees_lst = []
        user_id = request.user.id
        tree_planted_by_user = PlantedTree.objects.filter(user_id=user_id).all()

        for tree_planted in tree_planted_by_user:
            trees_lst.append({
                'tree': tree_planted.tree.name,
                'age': tree_planted.age,
                'scientific_name': tree_planted.tree.scientific_name,
                'user': tree_planted.user.username,
                'account': tree_planted.account.name,
            })

        trees_lst = [model_to_dict(tree_planted) for tree_planted in tree_planted_by_user]

        return JsonResponse(trees_lst, status=200, safe=False)
