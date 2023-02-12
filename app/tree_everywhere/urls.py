from django.urls import path

from app.tree_everywhere.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]
