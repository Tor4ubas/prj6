from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user_app.models import User

admin.site.register(User)

# Отмена регистрации модели User
admin.site.unregister(User)


# Зарегистрировать модель User с новым классом администратора
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'is_active')
    list_filter = ('is_active',)
    actions = ['deactivate_users', 'activate_users']

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_users.short_description = "Деактивировать выбранных пользователей"

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)
    activate_users.short_description = "Активировать выбранных пользователей"