from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from api import views

urlpatterns = [
                  path('categories/', views.categoryApi),
                  path('categories/<int:id>', views.categoryApi),
                  path('users/', views.userApi),
                  path('users/<int:id>', views.userApi),
                  path('articles/', views.articleApi),
                  path('articles/<int:id>', views.articleApi),
                  path('articles/save-file/', views.save_file),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
