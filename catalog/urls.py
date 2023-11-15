from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', views.catalog_list, name='catalog_list'),
    path('contacts/', views.contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
