from django.urls import path
from book_buddy import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chapter_reflect', views.chapter_reflect, name='chapter_reflect'),
]