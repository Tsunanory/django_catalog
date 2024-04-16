from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from blog.models import Post

class PostListView(ListView):
    model = Post
    # template_name = 'blog/product.html' ##########

class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', )
    success_url = reverse_lazy('posts:list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', )
    success_url = reverse_lazy('posts:list')


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
