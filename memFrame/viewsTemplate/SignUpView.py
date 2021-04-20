from django.shortcuts import render
from django.views.generic import TemplateView

from memFrame.forms.SignUpForm import SignUpForm
from memFrame.service.UserService import UserService

'''
Welcomeページのビュー
@author Nozawa
'''
class SignUpView(TemplateView):
    #ユーザーサービスクラス
    userService:UserService = UserService()
    template_name = 'memFrame/SignUp.html'
    def __init__(self):
        self.params = {
            'form': SignUpForm(),
        }

    def get(self, request):
        return render(request, 'memFrame/SignUp.html', self.params)

    # ユーザー登録フォームを表示する
    def post(self, request):
        #登録をする
        self.userService.createCommonUser(request)
        # メッセージを代入
        self.params['resultMessage'] = "登録処理が完了しました！"
        return render(request, 'memFrame/SignUp_Complete.html', self.params)