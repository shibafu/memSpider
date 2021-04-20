"""django_app URL Configuration
ユーザー登録
他は基本的にののURL定義
"""
from django.urls import path

from memFrame.viewsTemplate.WelcomeView import WelcomeView
from memFrame.viewsTemplate.mockup.UserSignUpView import UserSignUpView

urlpatterns = [
    path('Welcome', WelcomeView.as_view(), name='Welcome'),  # ユーザー登録ページ

]