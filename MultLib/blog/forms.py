from django import forms
from .models import UserBook, Post, Genre

class UserBookForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ['user_book_title',
                  'user_book_cover',
                  'user_book_author',
                  'user_book_genre',
                  'user_book_description',
                  'user_book_body',
                  'user_book_status',
                  'user_book_publish',
                  'user_book_pages',
                  'user_book_language',
                  'user_book_age',
                  ]
        
        widgets = {'user_book_title': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Название книги...'}),
                    'user_book_description': forms.Textarea(attrs={'class': 'form-control',
                                                    'placeholder': 'Описание книги...'}),
                    'user_book_language': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Язык книги'}),
                    'user_book_status': forms.Select(choices=[('Draft', 'Черновик'), 
                                                                   ('published', 'Опубликовано')]),
                    'user_book_body': forms.Textarea(attrs={'class': 'form-control',
                                                    'placeholder': 'Текст книги...'}),
                    'user_book_age': forms.NumberInput(attrs={'min': '0', 'max': '18',
                                                    'placeholder': 'Возрастное ограничение: 0-18 лет'}),
                    'user_book_genre': forms.CheckboxSelectMultiple(choices=[
                        (g.genre_slug, g.genre_title) for g in Genre.objects.all()
                        ]),
                    'user_book_pages': forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Количество страниц....'}),
                    }
        
        labels = {'user_book_title': 'Название книги',
                  'user_book_cover': 'Обложка',
                  'user_book_author': 'Автор книги',
                  'user_book_genre': 'Жанры',
                  'user_book_description': 'Описание',
                  'user_book_body': 'Содержание',
                  'user_book_status': 'Статус написания',
                  'user_book_publish': 'Дата публикации',
                  'user_book_pages': 'Кол-во страниц',
                  'user_book_language': 'Язык книги',
                  'user_book_age': 'Возрастная категория',
                  }
        
        error_messages = {'user_book_title': {
            'max_length': 'Слишком длинное название!'
            },
            'user_book_age': {
                'min_value': 'Некорректное значение',
                'max_value': 'Некорректное значение',
            }
        }
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'body',
                  'status',
                  ]
        
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control',
                                        'placeholder': 'Название поста'}),
                                        }
