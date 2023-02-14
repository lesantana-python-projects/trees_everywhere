from django.urls import path
from django.views.generic import RedirectView

from .views import LoginView

urlpatterns = [
    path('', RedirectView.as_view(url='/tree', permanent=True)),
    path('login/', LoginView.as_view(), name='login'),
]
