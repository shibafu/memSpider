from django.shortcuts import render
from django.views.generic import TemplateView

from memFrame.ModelForm import UserSignUpForm
from memFrame.forms.SignInForm import UserSignInForm
from memFrame.service import UserService

'''
サインインビュー
@author Nozawa
'''


class UserSignInView(TemplateView):
    #ユーザーサービスクラス
    userService:UserService = UserService.UserService()
    #初期化処理
    def __init__(self):
        self.params = {
            'form': UserSignInForm(),
            'userToken': None,
        }
    # ユーザー登録フォームを表示する
    def get(self, request):
        # 画像オブジェクトを代入
        return render(request, 'memFrame/mock_SignIn.html', self.params)

    # ユーザー登録フォームを表示する
    def post(self, request):
        #認証をする
        UserToken = self.userService.signInUser(request)
        # メッセージを代入
        self.params['resultMessage'] = "登録処理が完了しました！"
        self.params['userToken'] = request
        return render(request, 'memFrame/mock_SignIn.html', self.params)