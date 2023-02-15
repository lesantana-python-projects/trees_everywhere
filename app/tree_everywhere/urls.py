from django.urls import path

from app.tree_everywhere.views.index import IndexView
from app.tree_everywhere.views.tree import TreeList
from app.tree_everywhere.views.tree_planted import (PlantTreeCreate, PlantTreeList)

urlpatterns = [
    path('', IndexView.as_view(), name='tree_everywhere_home'),
    path('to_plant', PlantTreeCreate.as_view(), name='tree_everywhere_to_plant'),
    path('planted', PlantTreeList.as_view(), name='tree_everywhere_planted'),
    path('trees', TreeList.as_view(), name='tree_everywhere_trees')
]
