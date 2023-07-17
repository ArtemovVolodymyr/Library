from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('home.urls')),
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('', include('author.urls')),
    path('', include('book.urls')),
    path('', include('order.urls')),
]

