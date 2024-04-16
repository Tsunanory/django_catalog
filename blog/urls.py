from django.urls import path

from blog.views import BlogConfig, PostCreateView
app_name = BlogConfig.name
# from blog.views import PostListView

urlpatterns = [
    # path('', PostListView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('view/<int:pk>/', ..., name='view'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='delete'),

]

