from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from memFrame.forms.SignInForm import SignInForm
from memFrame.service.UserService import UserService

'''
Welcomeページのビュー
@author Nozawa
'''
class SignInView(TemplateView):
    #ユーザーサービスクラス
    userService:UserService = UserService()
    template_name = 'memFrame/SignIn.html'
    def __init__(self):
        self.params = {
            'form': SignInForm(),
        }

    def get(self, request):
        #カラムを指定して取り出す
        return render(request, 'memFrame/SignIn.html', self.params)
    # ユーザー登録フォームを表示する
    def post(self, request):
        #認証をする
        request = self.userService.signInUser(request)
        #カラムを指定して取り出す
        return redirect('/home/')