from django.contrib import admin
from .models import Post
from .models import Book
from .models import Commentary

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
class BookAdmin:
  list_display = ['title', 'author', 'publish', 'status', 'slug']
  list_filter = ['author', 'status', 'publish', 'created']
  search_fields = ['title', 'body']
  date_hierarchy = 'publish'
  ordering = ['status', 'publish']
  raw_id_fields = ['author']
  prepopulated_fields = {'slug': ('title',)}

@admin.register(Commentary)
class CommAdmin:
  raw_id_fields = ['author']
