
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Organization, TaxSystem, Document

print(list(set([f.name for f in Organization._meta.fields])))

UserAdmin.fieldsets = (
    ('Данные', {'fields': ('email', "organization_type", 'first_name',
     'last_name', 'middle_name', 'phone', "inn", "ogrn", "tax_system",)}),

    ('Регистрационные данные', {'fields': ('username', 'password')}),
    ('Права', {'fields': (
        'is_active',
        'is_staff',
        'is_superuser',
        # 'groups',
        # 'user_permissions'
    )}),
)


class ProfileInline(admin.StackedInline):
    model = Document
    extra = 1


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Organization
    list_display = ['email', 'username',]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', "organization_type", 'first_name', 'last_name', 'middle_name', 'password1', 'password2', 'phone', 'inn', "ogrn", "tax_system")}
         ),
    )
    inlines = [ProfileInline]


admin.site.register(Organization, CustomUserAdmin)
admin.site.register(TaxSystem)
