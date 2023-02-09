from django.urls import path
from gpt3 import views

urlpatterns = [
    path('', views.gpt3, name='gpt3'),
]