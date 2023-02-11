from django.urls import path
from .views import TreeList

urlpatterns = [
    path('tree', TreeList.as_view(), name="tree"),
]
