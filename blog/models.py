from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=50, verbose_name='slug', default=None)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='posts/', verbose_name='превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_posted = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
