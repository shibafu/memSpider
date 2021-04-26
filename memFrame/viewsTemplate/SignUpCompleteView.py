from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from memFrame.forms.SignInForm import SignInForm
from memFrame.service.UserService import UserService

'''
Welcomeページのビュー
@author Nozawa
'''
class SignUpCompleteView(TemplateView):
    #ユーザーサービスクラス
    userService:UserService = UserService()
    template_name = 'memFrame/SignUp_Complete.html'
    def __init__(self):
        self.params = {
            'form': SignInForm(),
        }

    def get(self, request):
        #カラムを指定して取り出す
        return render(request, 'memFrame/SignUp_Complete.html', self.params)