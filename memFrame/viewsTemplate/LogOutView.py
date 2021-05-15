from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from memFrame.forms.SignUpForm import SignUpForm
from memFrame.service.UserService import UserService

'''
ログアウトページのビュー
@author Nozawa
'''
class LogOutView(TemplateView):
    #ユーザーサービスクラス
    userService:UserService = UserService()
    def __init__(self):
        self.params = {
            'form': SignUpForm(),
        }

    def get(self, request):
        self.userService.logOut(request)
        return redirect('https://memspider.com/')
