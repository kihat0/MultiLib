from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth
from blog import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    #path('blog/login/', user_view.Login, name='login'),
    path('blog/logout/', auth.LogoutView.as_view(template_name='blog/Main_Page/index.html'), name='logout'),
    #path('blog/register/', user_view.registr, name='registr'),
]
