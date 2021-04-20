from django.shortcuts import render
from django.views.generic import TemplateView
import json

from memFrame.forms.PictUploadForm import PictUploadForm
from memFrame.models import M_User
from memFrame.service.PictService import PictService
from memFrame.service.UserService import UserService

'''
Welcomeページのビュー
@author Nozawa
'''


class PictUploadView(TemplateView):
    template_name = 'memFrame/PictUpload.html'
    # ユーザーサービスクラス
    userService: UserService = UserService()
    # ユーザーサービスクラス
    pictService: PictService = PictService()

    def __init__(self):
        self.params = {
            'form': PictUploadForm()
        }

    def get(self, request):
        # カラムを指定して取り出す
        return render(request, 'memFrame/PictUpload.html', self.params)

    # 画像フォームを表示する
    def post(self, request):
        # 認証処理
        userToken = json.loads(request.session.get('AuthenticateToken'))
        authedUser: M_User = self.userService.serchUserByToken(userToken['AuthenticateToken'])

        # 画像登録
        self.pictService.createFromRequest(request, authedUser)

        # 画像オブジェクトを代入
        self.params['resultMessage'] = "登録処理が完了しました！"
        return render(request, 'memFrame/PictUpload.html', self.params)
