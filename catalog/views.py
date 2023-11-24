from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import BlogPost

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

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)  # Фильтруем только опубликованные статьи
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1  # Увеличиваем счетчик просмотров
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/create.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/edit.html'
    fields = ['title', 'content', 'is_published']

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:list')
    context_object_name = 'post'
