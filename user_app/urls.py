from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user_app.apps import UserConfig
from user_app.views import RegisterView, UserUpdateView, generate_new_password, register_confirm, \
    VerifiedEmailView

app_name = UserConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),

    # Функция сменить пароль на рандомный
    path('profile/genpassword', generate_new_password, name='generate_new_password'),

    # Верификация почты
    path('verified_email/', VerifiedEmailView.as_view(), name='verified_email'),
    path('register_confirm/<str:token>/', register_confirm, name='register_confirm'),
]