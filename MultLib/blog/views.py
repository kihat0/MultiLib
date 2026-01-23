from django.shortcuts import render
from .models import Post
from .models import Book
from .models import UserBook
from .models import Rating
from django.http import Http404
from django.db.models import Avg
from django.db.models.functions import Coalesce

def post_list(request):
  posts = Post.published.all()
  return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
  post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
  return render(request, 'blog/post/detail.html', {'post': post})

def book_list(request):
  books = Book.book_published.all()
  return render(request, 'blog/book/list.html', {'books': books})

def book_detail(request, id):
  book = get_object_or_404(Book, id=id, status=Book.BookStatus.PUBLISHED)
  avg =  book.book_rating.aggregate(avarage = Coalesce(Avg('rating'), 0))['avarage']
  avg = round(avg, 1)
  return render(request, 'blog/book/detail.html', {'book': book, 'avg': avg})

def book_write_list(request):
  user_books = UserBook.user_book_published.all()
  return render(request, 'blog/book_write/list.html', {'user_books': user_books})

def book_write_detail(request, id):
  user_book = get_object_or_404(UserBook, id=id, status=UserBook.UserBookStatus.PUBLISHED)
  return render(request, 'blog/book_write/detail.html', {'user_book': user_book})
