from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('', include('djoser.urls')),
        path('', include('djoser.urls.authtoken')),
        path('', include('api.urls'))
    ]))
]
