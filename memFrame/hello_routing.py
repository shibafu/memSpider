"""django_app URL Configuration
hello の仕様URL
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Welcomeページ
    path('next', views.next, name='next'),  # 次へページ

]