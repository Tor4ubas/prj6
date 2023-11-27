from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_form.html'
    fields = ('title', 'content', 'preview', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj


class BlogPostListView(ListView):
    model = BlogPost
    # template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)

        # Выборка записей блога с пустым значением "slug" или NULL
        blog_posts_without_slug = queryset.filter(slug__isnull=True)

        # Удаление выбранных записей блога
        blog_posts_without_slug.delete()

        return queryset


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_form.html'
    fields = ('title', 'content', 'is_published',)

    def get_success_url(self):
        return reverse('blog:update_post', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
    context_object_name = 'post'





