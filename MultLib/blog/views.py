from django.shortcuts import render
from .models import Post
from .models import Book
from django.http import Http404

def post_list(request):
  posts = Post.published.all()
  return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
  post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
  return render(request, 'blog/post/detail.html', {'post': post})

def book_list(request):
  books = Book.b_published.all()
  return render(request, 'blog/book/list.html', {'books': books})

def book_detail(request, id):
  book = get_object_or_404(Book, id=id, status=Book.BookStatus.PUBLISHED)
  return render(request, 'blog/book/detail.html', {'book': book})

def book_write_list(request):
  books_write = BookWrite.bw_published.all()
  return render(request, 'blog/book_write/list.html', {'books_write': books_write})

def book_write_detail(request, id):
  book_write = get_object_or_404(BookWrite, id=id, status=BookWrite.BookWriteStatus.PUBLISHED)
  return render(request, 'blog/book_write/detail.html', {'book_write': book_write})
