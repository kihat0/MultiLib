from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .models import Book
from .models import UserBook
from .models import Rating
from .models import Edit_Profile
from .forms import UserBookForm, ProfileForm, UserEditForm, RatingForm, CreateUserForm
from django.db.models import Q
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'blog/book/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book_raiting = Book.book_raiting.all()
    count = book_raiting.count()
    if count > 0:
        avg = sum(Rating.rating for rating in book_raiting) / count
    else:
        avg = 0

    user_rating = None
    if request.user.is_authenticated:
        user_rating = Book.book_raiting.filter(user=request.user).first()
    cont = {
        'book': book,
        'user_rating': user_rating,
        'count': count,
        'avg': round(avg, 1)
    }
    return render(request, 'blog/book/book_detail.html', cont)

def user_book_list(request):
    user_books = UserBook.user_book_published.all()
    return render(request, 'blog/user_book/user_book_list.html', {'user_books': user_books})

def user_book_detail(request, id):
    user_book = get_object_or_404(UserBook, id=id, status=UserBook.UserBookStatus.PUBLISHED)
    return render(request, 'blog/user_book/user_book_detail.html', {'user_book': user_book})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = UserBookForm(request.POST)
        if form.is_valid():
            form.save()
            select_genre = form.cleaned_data['genres']
            return redirect(reverse('user_book_list'))
    else:
        form = UserBookForm()
        return render(request, 'blog/user_book/add_book/add_book.html', {'form': form})
        #return redirect(reverse('add_book'))
    
def index(request):
    return render(request, 'blog/Main_Page/index.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('blog/profile.html')
    else:
        user_form = UserEditForm(instance=request.user)
        try:
            profile_form = ProfileForm(instance=request.user.profile)
        except Edit_Profile.DoesNotExist:
            profile = Edit_Profile.objects.create(user=request.user)
            profile_form = ProfileForm(instance=profile)
    return render(request, 'blog/profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
    

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.none()
    if query:
        books = Book.objects.filter(
            Q(book_title__icontains=query)|
            Q(book_author__icontains=query)|
            Q(book_id__icontains=query)
        ).distinct()

    return render(request, 'blog/search_res.html', {'books': books, 'query':query})

@login_required
def add_rating(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    now_rating = Rating.objects.filter(user=request.user, book=book).first()

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            if now_rating:
                now_rating.rating = form.cleaned_data['rating']
                now_rating.save()
            else:
                Rating.objects.create(
                    user=request.user,
                    book=book,
                    rating=form.cleaned_data['rating']
                )
        return redirect('book_detail', book_id=book.book_id)
    
    else:
        if now_rating:
            form = RatingForm(instance=now_rating)
        else:
            form = RatingForm()

    return render(request, 'blog/book_detail.html', {'book': book,
                                                     'now_rating': now_rating,
                                                     'form': form})

def registr(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CreateUserForm()
    return render(request, 'blog/Main_Page/index.html', {'form': form})
