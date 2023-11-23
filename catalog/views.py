from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render


from catalog.models import Product


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_detail_url'] = self.request.path
        return context

def ProductCreateView(CreateView):
    pass


def ProductUpdateView(UpdateView):
    pass
