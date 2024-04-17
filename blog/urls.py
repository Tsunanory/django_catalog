from django.urls import path

from blog.views import PostCreateView, PostListView, PostDetailView, PostDeleteView, PostUpdateView

app_name = 'blog'
# from blog.views import PostListView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('', PostListView.as_view(), name='list'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]

