from django.contrib import admin
from .models import Tree


class TreeAdmin(admin.ModelAdmin):
    model = Tree
    list_display = ['name', 'scientific_name', 'created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('name', 'scientific_name', 'created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Tree, TreeAdmin)
