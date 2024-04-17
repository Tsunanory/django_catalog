from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content',)
    success_url = reverse_lazy('blog:list')


class PostListView(ListView):
    model = Post
    # template_name = 'blog/product.html' ##########


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', )
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')