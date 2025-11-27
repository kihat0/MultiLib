from django.contrib import admin
from .models import Post
from .models import Book
from .models import BookWrite


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
  list_display = ['b_title', 'b_author', 'b_publish', 'b_status', 'b_slug']
  list_filter = ['b_author', 'b_publish', 'b_created', 'isbn', 'b_age']
  search_fields = ['b_title', 'b_body']
  date_hierarchy = 'b_publish'
  ordering = ['b_publish']
  raw_id_fields = ['b_author']
  prepopulated_fields = {'b_slug': ('b_title',)}

@admin.register(BookWrite)
class BookWriteAdmin:
  list_display = ['bw_title', 'bw_author', 'bw_publish', 'bw_status', 'bw_slug']
  list_filter = ['bw_author', 'bw_publish', 'bw_created', 'bw_age']
  search_fields = ['bw_title', 'bw_body']
  date_hierarchy = 'bw_publish'
  ordering = ['bw_publish']
  raw_id_fields = ['bw_author']
  prepopulated_fields = {'bw_slug': ('bw_title',)}
