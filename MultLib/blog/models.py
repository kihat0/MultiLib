from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
class post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликован'
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, verbose_name='Метка')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Автор')
    body = models.TextField(verbose_name='Содержание')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')
    published = PubishedManager()

    class Meta:
        orderind = ('-publish')
        indexes = [
            models.Index(fields=['-publish']),
             ]
        verbose_name='Пост'
        verbose_name_plural='Посты'
        
    def __str__(self):
        return self.title


class book(models.Model):
    class BookStatus(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'
    b_title = models.CharField(max_length=100, verbose_name='Название книги')
    b_slug = models.SlugField(max_length=100, verbose_name='Метка книги')
    b_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Автор книги')
    b_body = models.TextField(verbose_name='Содержание книги')
    b_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    b_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    b_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    b_status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')
    b_published = PubishedManager()

    class Meta:
        orderind = ('-publish')
        indexes = [
            models.Index(fields=['-publish']),
            ]
        verbose_name='Книга'
        verbose_name_plural='Книги'
        
    def __str__(self):
        return self.title




