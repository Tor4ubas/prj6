from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import OuterRef, Subquery
#from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
#from django.forms import inlineformset_factory

from catalog.models import Product, Version
from catalog.forms import ProductForm
from catalog.forms import VersionForm


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


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    active_version = product.version_set.filter(is_active=True).first()
    versions = product.version_set.all()

    return render(request, 'catalog/product_detail.html',
                  {'product': product, 'active_version': active_version, 'versions': versions})


class ProductCreateView(LoginRequiredMixin, View):
    form_class = ProductForm
    template_name = 'catalog/create_product.html'
    version_form = VersionForm()

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'version_form': self.version_form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('catalog:product_detail', pk=product.id)
        else:
            return render(request, self.template_name, {'form': form, 'version_form': self.version_form})


class ProductEditView(LoginRequiredMixin, View):
    form_class = ProductForm
    template_name = 'catalog/product_edit.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        # Проверяем, является ли текущий пользователь владельцем продукта
        if product.owner != request.user:
            return render(request, 'catalog/error.html', {'message': 'Вы не имеете прав для редактирования'})

        form = self.form_class(instance=product)
        return render(request, self.template_name, {'form': form, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        # Проверяем, является ли текущий пользователь владельцем продукта
        if product.owner != request.user:
            return render(request, 'error.html', {'message': 'You are not the owner of this product.'})

        form = self.form_class(request.POST or None, instance=product)

        if form.is_valid():
            product = form.save(commit=False)
            publication_status = request.POST.get('publication_status')
            print(publication_status)  # Отладочный вывод
            product.is_published = publication_status == 'published'  # Обновление статуса публикации
            product.save()
            return redirect('catalog:product_detail', pk=pk)

        return render(request, self.template_name, {'form': form, 'product': product})


def product_confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('catalog:catalog_list')
    return render(request, 'catalog/product_confirm_delete.html', {'product': product})