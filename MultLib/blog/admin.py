from django.contrib import admin
from django import forms
from .services import parsing
from .models import Post
from .models import Book
from .models import UserBook
from .models import Genre
from .models import Commentary_Book
from .models import Commentary_Book_Write
from .models import Rating
from .models import Author, Edit_Profile

class BookAdminForm(admin.ModelAdmin):
  gutenberg = forms.CharField(max_length=10,
                              label='Айди книги',
                              required=False)
  class Meta:
    model = Book
    fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'publish', 'status', 'slug']
  list_filter = ['author', 'status', 'publish', 'created']
  search_fields = ['title', 'body']
  date_hierarchy = 'publish'
  ordering = ['status', 'publish']
  raw_id_fields = ['author']
  prepopulated_fields = {'slug': ('title',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  form = BookAdminForm
  list_display = ['book_title', 'book_author', 'book_publish', 'book_status', 'book_slug']
  list_filter = ['book_author', 'book_publish', 'book_created', 'isbn', 'book_age']
  search_fields = ['book_title', 'book_body']
  date_hierarchy = 'book_publish'
  ordering = ['book_publish']
  raw_id_fields = ['book_author']
  prepopulated_fields = {'book_slug': ('book_title',)}

@admin.register(UserBook)
class BookWriteAdmin(admin.ModelAdmin):
  list_display = ['user_book_title', 'user_book_author', 'user_book_publish', 'user_book_status', 'user_book_slug']
  list_filter = ['user_book_author', 'user_book_publish', 'user_book_created', 'user_book_age']
  search_fields = ['user_book_title', 'user_book_body']
  date_hierarchy = 'user_book_publish'
  ordering = ['user_book_publish']
  raw_id_fields = ['user_book_author']
  prepopulated_fields = {'user_book_slug': ('user_book_title',)}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
  prepopulated_fields = {'genre_slug': ('genre_title',)}

@admin.register(Commentary_Book_Write)
class CommentAdmin(admin.ModelAdmin):
  list_filter = ['comment_user_book_author', 'comment_user_book_publish']
  search_fields = ['comment_user_book_body']
  raw_id_fields = ['comment_user_book_author']
  date_hierarchy = 'comment_user_book_publish'
  
@admin.register(Commentary_Book)
class CommentAdmin(admin.ModelAdmin):
  list_filter = ['comment_book_author', 'comment_book_publish']
  search_fields = ['comment_book_body']
  raw_id_fields = ['comment_book_author']
  date_hierarchy = 'comment_book_publish'

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
  pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass

@admin.register
class EditProfileAdmin(admin.ModelAdmin):
  pass
