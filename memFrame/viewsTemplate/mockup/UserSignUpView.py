from django.shortcuts import render
from django.views.generic import TemplateView

from memFrame.ModelForm import UserSignUpForm
from memFrame.service import UserService

'''
一般ユーザーを登録する
@author Nozawa
'''


class UserSignUpView(TemplateView):
    #ユーザーサービスクラス
    userService:UserService = UserService.UserService()
    #初期化処理
    def __init__(self):
        self.params = {
            'form': UserSignUpForm.UserSignUpForm(),
        }
    # ユーザー登録フォームを表示する
    def get(self, request):
        # 画像オブジェクトを代入
        return render(request, 'memFrame/mock_SignUp.html', self.params)

    # ユーザー登録フォームを表示する
    def post(self, request, **kwargs):
        #ユーザーを登録する
        self.userService.createCommonUser(request)

        # メッセージを代入
        self.params['resultMessage'] = "登録処理が完了しました！"
        return render(request, 'memFrame/mock_SignUp.html', self.params)