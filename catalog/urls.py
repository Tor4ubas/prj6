from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
