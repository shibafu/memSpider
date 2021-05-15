'''
ユーザーの編集を行うサービスです
@author Nozawa
'''
from django.contrib.auth.hashers import make_password
from django.core import serializers

from memFrame.Authenticate.MemFrameAuthenticateBackEnd import MemFrameBackAuthenticateEnd
from memFrame.DTO.UserTokenDto import T_UserTokenDto
from memFrame.models import T_UserToken
from memFrame.models.M_User import M_User

import base64
import datetime
import json

class UserService:
    _authService:MemFrameBackAuthenticateEnd = MemFrameBackAuthenticateEnd()
    #一般ユーザーを新規登録する
    def createCommonUser(self, request):
        # ユーザーマネージャーからユーザーを登録する
        # パスワードをハッシュにセット
        userObj = M_User()
        # ユーザー属性を一般、スタッフでないに設定
        userObj.isSuperuser = False
        userObj.updateDate = datetime.datetime.today()
        userObj.deleteFlg = False
        userObj.bannedFlg = False
        #パスワードをハッシュ化して設定
        userObj.set_password(request.POST['password'])
        userObj.username = request.POST['username']
        userObj.email = request.POST['email']

        # 値が正しいか確認(バリデーション)
        # 未実装
        userObj.save()
        # 値をDBへの登録

    #一般ユーザーを新規登録する
    def createSuperUser(self, request):
        userObj = M_User()
        # ユーザー属性をスーパーユーザー、スタッフでないに設定
        userObj.isSuperuser = True
        userObj.updateDate = datetime.datetime.today()
        userObj.deleteFlg = False
        userObj.bannedFlg = False

        #パスワードをハッシュ化して設定
        userObj.set_password(request.POST['password'])
        userObj.username = request.POST['username']
        userObj.email = request.POST['email']

        #パスワードをハッシュ化
        userObj.save()

        # 値が正しいか確認(バリデーション)
        # 未実装
        userObj.errors
        # 値をDBへの登録

    #認証処理を行う
    def signInUser(self, request):
        # メールアドレス、パスワードを取得
        name_or_mail = request.POST['name_or_mail']
        password = request.POST['password']
        userCresidented = self._authService.authenticate(request,
                                                         username=name_or_mail,
                                                         password=password)

        # 認証
        if userCresidented is None:
            return None
        # 認証トークンを作成
        authenticateToken = self._authService.createAuthToken(user=userCresidented)

        #画面保存用
        sesseonToken = T_UserTokenDto()

        sesseonToken.id = authenticateToken.id
        sesseonToken.AuthenticateToken = base64.b64encode(authenticateToken.AuthenticateToken).decode('utf-8')
        sesseonToken.role = authenticateToken.role
        sesseonToken.applyDateStart = authenticateToken.applyDateStart.strftime('%Y/%m/%d %H:%M')
        sesseonToken.applyDateEnd = authenticateToken.applyDateEnd.strftime('%Y/%m/%d %H:%M')

        # 認証トークンをJSON化
        jsonedToken = json.dumps(sesseonToken.__dict__)

        # トークンをセッションに保存
        request.session['AuthenticateToken'] = jsonedToken

        return request

    #認可処理を行う
    #未実装
    #def authUser(self, request):
    #    #DBから認証トークン情報を取得
    #    jsonedToken = request.session['AuthenticateToken']
    #    #有効開始期間が今日より先
    #    tokenObj:T_UserToken = serializers.deserialize(T_UserToken, jsonedToken)
    #     if(tokenObj.applyDateStart > datetime.now):
    #         #例外
    #         return None;
    #     #有効終了機関が今日より後
    #     elif(tokenObj.applyDateStart > datetime.now):
    #         #例外
    #         return None;
    #
    #     #Trueを返す
    #     return tokenObj;

    #ユーザートークンを削除し、ログアウトする
    def logOut(self, request):
        #DBから認証トークン情報を取得
        jsonedToken = request.session.get('AuthenticateToken')
        #有効開始期間が今日より先
        tokenInDB = base64.b64decode(jsonedToken)
        userToken:T_UserToken = T_UserToken.objects.filter(AuthenticateToken=tokenInDB, applyDateEnd__gte=datetime.datetime.now())

        #DBからユーザートークンを削除
        userToken.delete()

        # セッション&クッキー 削除
        request.session.flush()
        return None

    #Idでユーザーを取得します
    def serchUserById(self, id):
        return M_User.objects.filter(pk=id)

    #認証トークンでユーザーを取得します
    def serchUserByToken(self, hashToken):
        #ユーザートークンを取得
        tokenInDB = base64.b64decode(hashToken)
        userToken:T_UserToken = T_UserToken.objects.filter(AuthenticateToken=tokenInDB, applyDateEnd__gte=datetime.datetime.now())

        return M_User.objects.filter(UserTokenId=userToken[0].id)[0]
