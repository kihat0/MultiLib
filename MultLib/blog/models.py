from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class PublishedManagerBook(models.Manager):
    def get_queryset_b(self):
        return super().get_queryset().filter(status=Book.BookStatus.PUBLISHED)
    
class PublishedManagerBookWrite(models.Manager):
    def get_queryset_bw(self):
        return super().get_queryset().filter(status=BookWrite.BookWriteStatus.PUBLISHED)
        
class Post(models.Model):
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
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
             ]
        verbose_name='Пост'
        verbose_name_plural='Посты'
        
    def __str__(self):
        return self.title

class Book(models.Model):
    class BookStatus(models.TextChoices):
        PUBLISHED = 'PB', 'Опубликовано'
    b_title = models.CharField(max_length=150, db_index=True, verbose_name='Название книги')
    b_slug = models.SlugField(max_length=150, db_index=True, verbose_name='Метка книги')
    b_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_books', db_index=True, verbose_name='Автор книги')
    b_status = models.CharField(max_length=0, choices=BookStatus.Choices, default=BookStatus.PUBLISHED, verbose_name='Статус')
    b_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    b_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    b_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    b_cover = models.ImageField('cover/', blank=True, null=True)
    b_pages = models.PositiveIntegerField(verbose_name='Количество страниц', default=0)
    b_language = models.CharField(max_length=35, default='Русский', verbose_name='Язык')
    b_description = models.TextField(verbose_name='Описание книги')
    b_age = models.PositiveIntegerField(verbose_name='Возрастное ограничение', default=0)
    isbn = models.CharField(max_length=17, blank=True, null=True, unique=True, db_index=True, verbose_name='ISBN')
    b_published = PublishedManagerBook()

    class Meta:
        ordering = ['-b_publish']
        indexes = [
            models.Index(fields=['-b_publish']),
            ]
        verbose_name='Книга'
        verbose_name_plural='Книги'
        
    def __str__(self):
        return self.b_title

class BookWrite(models.Model):
    class BookWriteStatus(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'
    bw_title = models.CharField(max_length=100, db_index=True, verbose_name='Название книги')
    bw_slug = models.SlugField(max_length=100, db_index=True, verbose_name='Метка книги')
    bw_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_books_write', db_index=True, verbose_name='Автор книги')
    bw_body = models.TextField(verbose_name='Содержание книги')
    bw_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    bw_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    bw_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    bw_status = models.CharField(max_length=2, choices=BookWriteStatus.choices, default=BookWriteStatus.DRAFT, verbose_name='Статус')
    bw_cover = models.ImageField('cover/', blank=True, null=True)
    bw_pages = models.PositiveIntegerField(verbose_name='Количество страниц', default=0)
    bw_language = models.CharField(max_length=35, default='Русский', verbose_name='Язык')
    bw_description = models.TextField(verbose_name='Описание книги')
    bw_age = models.PositiveIntegerField(verbose_name='Возрастное ограничение', default=0)
    bw_published = PublishedManagerBookWrite()

    class Meta:
        ordering = ['-bw_publish']
        indexes = [
            models.Index(fields=['-bw_publish']),
            ]
        verbose_name='Книга пользователя'
        verbose_name_plural='Книги пользователей'
        
    def __str__(self):
        return self.bw_title

class Commentary(models.Model):
    c_body = models.TextField(verbose_name='комментарий')     
    c_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    c_update = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    c_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comm', verbose_name='Автор')
    c_published = PublishedManager()

    class Meta:
        ordering = ['-c_publish']
        indexes = [
            models.Index(fields=['-c_publish']),
            ]
        verbose_name='Комментарии'
        verbose_name_plural='Комметарии'

    def __str__(self):
        return self.c_author
        
