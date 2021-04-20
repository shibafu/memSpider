"""django_app URL Configuration
ユーザー登録
他は基本的にののURL定義
"""
from django.urls import path

from memFrame.viewsTemplate.SignInView import SignInView
from memFrame.viewsTemplate.SignUpView import SignUpView

urlpatterns = [
    path('/signup/', SignUpView.as_view(), name='signup'),  # ユーザー登録ページ
    path('/signin/', SignInView.as_view(), name='signin'),  # ユーザーサインインページ

]