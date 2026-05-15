from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Category
from django.views.generic import DetailView

# Представление для вывода списка статей

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        return context


# Create your views here.

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context

class PostFromCategory(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    category = None
    def get_queryset(self):
        self.category = get_object_or_404(klass = Category, slug=self.kwargs['slug'])
        queryset = Post.objects.filter(category=self.category)

        if not queryset:
            sub_cat = Category.objects.filter(parent = self.category)
            queryset = Post.objects.filter(category__in = sub_cat)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Записи из категории: {self.category.title}'
        page= context['page_obj']
        context['pagination_range'] = page.paginator.get_elided_page_range(page.number)
        return context
