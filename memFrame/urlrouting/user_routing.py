"""django_app URL Configuration
ユーザー登録
他は基本的にののURL定義
"""
from django.urls import path

from memFrame.viewsTemplate.HomeView import HomeView
from memFrame.viewsTemplate.mockup.UserSignUpView import UserSignUpView

urlpatterns = [
    path('Home', HomeView.as_view(), name='Home'),  # ユーザーホーム

]