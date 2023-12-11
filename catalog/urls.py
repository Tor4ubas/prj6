from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views, versions
from .views import ContactsView, CatalogListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
                  path('', CatalogListView.as_view(), name='catalog_list'),
                  path('contacts/', ContactsView.as_view(), name='contacts'),
                  path('catalog/', CatalogListView.as_view(), name='catalog_list'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
                  path('create/', views.product_create, name='create_product'),
                  path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
                  path('product/<int:pk>/delete/', views.product_confirm_delete, name='product_confirm_delete'),
                  # path('create_product/', views.create_product, name='create_product'),
                  path('product/<int:pk>/versions/', versions.version_list, name='version_list'),
                  path('product/<int:pk>/versions/create/', versions.version_create, name='version_create'),
                  path('versions/<int:pk>/activate/', versions.version_active, name='version_active'),
                  path('versions/<int:pk>/version_delete/', versions.version_delete, name='version_delete'),
                  path('versions/<int:pk>/versions/confirm_delete_version/', versions.confirm_delete_version,
                       name='confirm_delete_version'),
                  path('version/make_active/<int:pk>/', versions.make_active, name='make_active'),
                  # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
                  # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
                  # path('register/', user_app.views.register_user, name='register'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
