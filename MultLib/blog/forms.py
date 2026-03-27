from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserBook, Post, Genre, Commentary_Book_Write, Commentary_Book, Edit_Profile, Rating

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
        
        widgets = {'user_book_title': forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                            'placeholder': 'Название книги...',
                                                            'required': True,
                                                            'data-bs-toggle': 'tooltip',
                                                            'maxlength': '200',
                                                            'title': 'Введите название книги'}),
                    'user_book_description': forms.Textarea(attrs={'class': 'form-control',
                                                            'placeholder': 'Описание книги...',
                                                            'max_length': '2000',
                                                            'rows': 6,
                                                            'style': 'resize: vertical;',}),
                    'user_book_language': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Язык книги'}),
                    'user_book_status': forms.Select(attrs={'class': 'form-select form-select-lg'}),

                    'user_book_body': forms.Textarea(attrs={'class': 'form-control',
                                                            'placeholder': 'Текст книги...',
                                                            'rows': 20,
                                                            'spellcheck': 'true'}),
                    'user_book_age': forms.NumberInput(attrs={'class': 'form-control',
                                                              'min': '0', 
                                                              'max': '18',
                                                              'placeholder': 'Возрастное ограничение: 0-18 лет',
                                                              'step': '1'}),
                    'user_book_genre': forms.CheckboxSelectMultiple(choices=[
                        (g.genre_slug, g.genre_title) for g in Genre.objects.all()
                        ]),
                    'user_book_pages': forms.TextInput(attrs={'class': 'form-control',
                                                              'min': '1',
                                                              'max': '999',
                                                              'placeholder': 'Количество страниц...',
                                                              'step': '1'}),
                    'user_book_cover': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                                'accept': 'image/*',
                                                                'data-bs-toggle': 'tooltip',
                                                                'title': 'Выберите картинку для обложки'}),
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
            },
            'user_book_description': {
                'max_length': 'Превышена допустимая длина',
            },
        }
        

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

        widgets = {'rating': forms.RadioSelect(attrs={'class': 'rating-radio'})}
class CommentToUserBookForm(forms.ModelForm):
    class Meta:
        model = Commentary_Book_Write
        fields = ['comment_user_book_body']

        widgets = {'comment_user_book_body': forms.Textarea(attrs={'class': 'form-control',
                                                                   'placeholder': 'Добавьте комментарий...'}),
                                                                   }
        
        labels = {'comment_user_book_body': 'Ваш комментарий',
                  }
        
        
class CommentToBookForm(forms.ModelForm):
    class Meta:
        model = Commentary_Book
        fields = ['comment_book_body']

        widgets = {'comment_book_body': forms.Textarea(attrs={'class': 'form-control',
                                                              'placeholder': 'Добавьте комментарий...'}),
                                                                   }
        
        labels = {'comment_book_body': 'Ваш комментарий',
                  }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Edit_Profile
        fields = ['nickname',
                'avatar',]
        
        widgets = {'nickname': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Введите никнейм...',
                                                    'max_length': '30'}),
                    'avatar': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                                'accept': 'image/*',
                                                                'data-bs-toggle': 'tooltip',
                                                                'title': 'Выберите картинку для обложки',}),
                    'birthday': forms.DateInput(attrs={'class': 'form-control',})}
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class CreateUserForm(UserCreationForm):
    email = {'email': forms.EmailField(required=True)}
    conf_pass = {'conf_pass': forms.CharField(widget=forms.PasswordInput(),
                                              label='Подтвердите пароль',
                                              required=True)}

    class Meta:
        model = User
        fields = ('email', 'password1', 'conf_pass', 'log_in')
        def check_pass2(self):
            password1 = self.cleaned_data.get('password1')
            conf_pass = self.cleaned_data.get('conf_pass')
            if password1 != conf_pass:
                raise forms.ValidationError('Пароли не совпадают!')
            return conf_pass
        
        def save_user(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


        
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
