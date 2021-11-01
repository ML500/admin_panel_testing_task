from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from api import views

urlpatterns = [
                  path('categories/', views.categoryApi, name='categories_list'),
                  path('categories/<int:id>', views.categoryApi, name='category_detail'),
                  path('users/', views.userApi, name='users_list'),
                  path('users/<int:id>', views.userApi, name='user_detail'),
                  path('articles/', views.articleApi, name='articles_list'),
                  path('articles/<int:id>', views.articleApi, name='article_detail'),
                  path('articles/save-file/', views.save_file),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
