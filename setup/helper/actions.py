from django.utils.translation import gettext_lazy as _


def set_all_to_active(modeladmin, request, queryset):
    queryset.update(active=True)


def set_all_to_deactivate(modeladmin, request, queryset):
    queryset.update(active=False)


set_all_to_active.short_description = _('Active all')
set_all_to_deactivate.short_description = _('Deactivate all')
