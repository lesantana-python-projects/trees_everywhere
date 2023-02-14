from django.urls import path

from app.tree_everywhere.views.index import IndexView
from app.tree_everywhere.views.tree_planted import PlantTreeCreate

urlpatterns = [
    path('', IndexView.as_view(), name='tree_everywhere_home'),
    path('plant', PlantTreeCreate.as_view(), name='tree_everywhere_plant')
]
