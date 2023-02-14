from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Account


class AccountInlineAdmin(admin.TabularInline):
    model = CustomUser.accounts.through
    extra = 0


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'about', 'joined']
    list_filter = ("username", "first_name")

    fieldsets = (
        (None, {'fields': ('first_name', 'username', 'joined')}),
        ('About', {
            'fields': ('about',)
        })
    )
    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'username', 'password1', 'password2')}),
        ('About', {
            'fields': ('about',)
        })
    )
    readonly_fields = ('joined',)
    inlines = (AccountInlineAdmin,)


class AccountAdmin(admin.ModelAdmin):
    model = Account


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
