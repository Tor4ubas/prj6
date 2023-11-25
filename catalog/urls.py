from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import create_product

from .views import ContactsView, CatalogListView, ProductDetailView

from catalog.views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView
)

app_name = 'catalog'+'blog'

urlpatterns = [
                  path('', CatalogListView.as_view(), name='catalog_list'),
                  path('contacts/', ContactsView.as_view(), name='contacts'),
                  path('catalog/', CatalogListView.as_view(), name='catalog_list'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
                  path('', BlogPostListView.as_view(), name='list'),
                  path('create/', BlogPostCreateView.as_view(), name='create'),
                  path('<slug:slug>/', BlogPostDetailView.as_view(), name='detail'),
                  path('<slug:slug>/update/', BlogPostUpdateView.as_view(), name='update'),
                  path('<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='delete'),
                  path('create/', create_product, name='create_product'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)