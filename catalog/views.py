from django.db.models import OuterRef, Subquery
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Product, Version
from catalog.templates.catalog.forms import ProductForm


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        active_versions = Version.objects.filter(product=OuterRef('pk'), is_active=True)
        queryset = super().get_queryset()
        queryset = queryset.annotate(active_version=Subquery(active_versions.values('version_name')[:1]))
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_detail_url'] = self.request.path
        return context


def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:catalog_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/create_product.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # Логика для метода POST (сохранение изменений)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_detail', pk=product.pk)
    else:
        # Логика для метода GET (отображение формы редактирования)
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_edit.html', {'form': form, 'product': product})


def product_confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('catalog:catalog_list')
    return render(request, 'catalog/product_confirm_delete.html', {'product': product})