import json
from django.shortcuts import render
from django.views.generic import TemplateView

from memFrame.forms.PictUploadForm import PictUploadForm
from memFrame.models import M_User
from memFrame.service.PictService import PictService
from memFrame.service.UserService import UserService

'''
Welcomeページのビュー
@author Nozawa
'''
class HomeView(TemplateView):
    template_name = 'memFrame/Home.html'
    #ユーザーサービスクラス
    userService:UserService = UserService()
    #ユーザーサービスクラス
    pictService:PictService = PictService()
    def __init__(self):
        self.params = {
            'username': '',
            'pictures': None,
        }

    def get(self, request):
        #認証処理
        userToken = json.loads(request.session.get('AuthenticateToken'))
        authedUser:M_User = self.userService.serchUserByToken(userToken['AuthenticateToken'])

        self.params['username'] = authedUser.username
        self.params['AuthenticateToken'] = userToken['AuthenticateToken']


        #画像検索処理
        pict_date = self.pictService.findByUser(user=authedUser)
        self.params['pictures'] = pict_date

        return render(request, 'memFrame/Home.html', self.params)