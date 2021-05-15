"""django_app URL Configuration
ユーザー登録
他は基本的にののURL定義
"""
from django.urls import path

from memFrame.viewsTemplate.LogOutView import LogOutView
from memFrame.viewsTemplate.SignInView import SignInView
from memFrame.viewsTemplate.SignUpCompleteView import SignUpCompleteView
from memFrame.viewsTemplate.SignUpView import SignUpView

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),  # サインインページ
    path('signup/', SignUpView.as_view(), name='signup'),  # ユーザー登録ページ
    path('signUpComplete/', SignUpCompleteView.as_view(), name='signUpComplete'),  # ユーザー登録完了ページ
    path('logout/', LogOutView.as_view(), name='logout'),  # ログアウト

]