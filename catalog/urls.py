from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import ContactsView, CatalogListView, ProductDetailView


app_name = 'catalog'

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalog_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogListView.as_view(), name='catalog_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
