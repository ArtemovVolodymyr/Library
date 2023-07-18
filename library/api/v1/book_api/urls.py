from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('book', views.BookDetailView)

urlpatterns = [
    path('', include(router.urls))

]
