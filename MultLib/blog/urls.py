from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('<int:id>/', views.post_detail, name='post_detail'),
  path('', views.book_list, name='book_list'),
  path('<int:id>/', views.book_detail, name='book_detail'),
  path('', views.book_write_list, name='book_write_list'),
  path('<int:id>/', views.book_write_detail, name='book_write_detail'),
]
