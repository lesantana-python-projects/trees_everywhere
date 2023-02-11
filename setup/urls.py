from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.tree_everywhere.urls')),
]

admin.site.site_header = 'YouShop Admin'
admin.site.index_title = 'YouShop Admin'
admin.site.site_title = 'YouShop Admin'
