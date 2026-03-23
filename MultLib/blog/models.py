from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class PublishedManagerBook(models.Manager):
    def get_queryset_b(self):
        return super().get_queryset().filter(status=Book.BookStatus.PUBLISHED)
    
class PublishedManagerUserBook(models.Manager):
    def get_queryset_bw(self):
        return super().get_queryset().filter(status=UserBook.UserBookStatus.PUBLISHED)
    
class PublishedManagerCommentToBook(models.Manager):
    def get_queryset_comment_book(self):
        return super().get_queryset().filter(status=Commentary_Book.comment_book_status)
        
class PublishedManagerCommentToUserBook(models.Manager):
    def get_queryset_comment_user_book(self):
        return super().get_queryset().filter(status=Commentary_Book_Write.comment_user_book_status)

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
    
    
class Author(models.Model):
    author_first_name = models.CharField(max_length=40, verbose_name='Имя автора')
    author_mid_name = models.CharField(max_length=40, verbose_name='Фамилия автора')
    author_last_name = models.CharField(max_length=40, verbose_name='Отчество автора')
    author_biography = models.TextField(verbose_name='Биография автора')
    author_image = models.ImageField('cover/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, verbose_name='Дата рождения')
    date_of_death = models.DateField(null=True, verbose_name='Дата смерти')

    class Meta:
        ordering = ['-author_mid_name']
        indexes = [
            models.Index(fields=['-author_mid_name']),
             ]
        verbose_name='Автор'

    def __str__(self):
        return self.author_mid_name


class Book(models.Model):
    class BookStatus(models.TextChoices):
        PUBLISHED = 'PB', 'Опубликовано'
    book_title = models.CharField(max_length=150, db_index=True, verbose_name='Название книги')
    book_slug = models.SlugField(max_length=150, db_index=True, verbose_name='Метка книги')
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_books', db_index=True, verbose_name='Автор книги', null=True, default=None)
    book_status = models.CharField(max_length=2, choices=BookStatus.choices, default=BookStatus.PUBLISHED, verbose_name='Статус')
    book_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    book_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    book_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    book_cover = models.ImageField('cover/', blank=True, null=True)
    book_pages = models.PositiveIntegerField(verbose_name='Количество страниц', default=0)
    book_language = models.CharField(max_length=35, default='Русский', verbose_name='Язык')
    book_description = models.TextField(verbose_name='Описание книги')
    book_age = models.PositiveIntegerField(verbose_name='Возрастное ограничение', default=0)
    book_genre = models.ManyToManyField('Genre', related_name='GenrA', verbose_name='Жанр')
    isbn = models.CharField(max_length=17, blank=True, null=True, unique=True, verbose_name='ISBN')
    book_published = PublishedManagerBook()

    class Meta:
        ordering = ['-book_publish']
        indexes = [
            models.Index(fields=['-book_publish']),
            ]
        verbose_name='Книга'
        verbose_name_plural='Книги'
        
    def __str__(self):
        return self.book_title

class UserBook(models.Model):
    class UserBookStatus(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'
    user_book_title = models.CharField(max_length=100, db_index=True, verbose_name='Название книги')
    user_book_slug = models.SlugField(max_length=100, db_index=True, verbose_name='Метка книги')
    user_book_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user_books', db_index=True, verbose_name='Автор книги')
    user_book_body = models.TextField(verbose_name='Содержание книги')
    user_book_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    user_book_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user_book_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    user_book_status = models.CharField(max_length=2, choices=UserBookStatus.choices, default=UserBookStatus.DRAFT, verbose_name='Статус')
    user_book_cover = models.ImageField('cover/', blank=True, null=True)
    user_book_pages = models.PositiveIntegerField(verbose_name='Количество страниц', default=0)
    user_book_language = models.CharField(max_length=35, default='Русский', verbose_name='Язык')
    user_book_description = models.TextField(verbose_name='Описание книги')
    user_book_age = models.PositiveIntegerField(verbose_name='Возрастное ограничение', default=0)
    user_book_genre = models.ManyToManyField('Genre', related_name='GenrU', verbose_name='Жанр')
    user_book_published = PublishedManagerUserBook()


    class Meta:
        ordering = ['-user_book_publish']
        indexes = [
            models.Index(fields=['-user_book_publish']),
            ]
        verbose_name='Книга пользователя'
        verbose_name_plural='Книги пользователей'
        
    def __str__(self):
        return self.user_book_title


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rate')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_rating')
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг')

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f'{self.book.book_title}: {self.rating}'
    
    
class Genre(models.Model):
    genre_title = models.CharField(max_length=66, unique=True, verbose_name='Название жанра')
    genre_slug = models.SlugField(max_length=66, unique=True, verbose_name='Метка жанра')
    genre_description = models.TextField(blank=True, verbose_name='Описание жанра')
    

    class Meta:
        ordering = ['genre_title']
        verbose_name='Жанр'
        verbose_name_plural='Жанры'

    def __str__(self):
        return self.genre_title
    

class Commentary_Book(models.Model):
    comment_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='CommentsB', verbose_name='Комментарий под книгу:', null=True)
    comment_book_body = models.TextField(verbose_name='комментарий')     
    comment_book_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    comment_book_update = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    comment_book_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_book_author', verbose_name='Автор')
    comment_book_status = models.BooleanField('Опубликовано', default=True)
    comment_book_published = PublishedManagerCommentToBook()

    class Meta:
        ordering = ['-comment_book_publish']
        indexes = [
            models.Index(fields=['-comment_book_publish']),
            ]
        verbose_name='Комментарии'
        verbose_name_plural='Комметарии'

    def __str__(self):
        return f'Комментарий от {self.comment_book_author}'


class Commentary_Book_Write(models.Model):
    comment_book_write = models.ForeignKey(UserBook, on_delete=models.CASCADE, related_name='CommentsBW', verbose_name='Комментарий под книгу:', null=True)
    comment_user_book_body = models.TextField(verbose_name='комментарий')     
    comment_user_book_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    comment_user_book_update = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    comment_user_book_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user_book_author', verbose_name='Автор')
    comment_user_book_status = models.BooleanField('Опубликовано', default=True)
    comment_user_book_published = PublishedManagerCommentToUserBook()

    class Meta:
        ordering = ['-comment_user_book_publish']
        indexes = [
            models.Index(fields=['-comment_user_book_publish']),
            ]
        verbose_name='Комментарии'
        verbose_name_plural='Комметарии'

    def __str__(self):
        return f'Комментарий от {self.comment_user_book_author}'
    
class Edit_Profile(models.Model):
    nickname = models.CharField(max_length=30, verbose_name='Никнейм')
    avatar = models.ImageField('cover/', blank=True, null=True, verbose_name='Сменить аватар')
    birthday = models.DateField(auto_now_add=True, verbose_name='Дата рождения')
        


