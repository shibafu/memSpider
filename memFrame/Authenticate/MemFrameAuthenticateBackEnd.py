from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.db.models import QuerySet

from config import settings
from memFrame.models import M_User, T_UserToken

"""
独自に実装した認証クラス
ユーザー名かメールアドレスで認証を行い
ユーザーオブジェクトを変換します
"""
class MemFrameBackAuthenticateEnd(BaseBackend):
    def get_user(self, user_id):
        try:
            return M_User.objects.get(pk=user_id)
        except M_User.DoesNotExist:
            return None
        # Check the username/password and return a user.
        ...
    #ユーザー名か、メールアドレスでユーザーを認証する
    def authenticate(self, request, username, password):
        #ユーザーネームでユーザーを取得
        user_by_names: QuerySet = M_User.objects.filter(username=username)
        #認証
        if user_by_names.count() > 0:
            valid_by_name = check_password(password, user_by_names[0].password)
            if valid_by_name:
                return user_by_names[0]
        #メールでユーザーを取得
        user_by_mails: QuerySet = M_User.objects.filter(email=username)

        if user_by_mails.count() > 0:
            #認証
            valid_by_mail = check_password(password, user_by_mails[0].password)
            if valid_by_mail:
                return user_by_mails[0]

        return None

    #認証トークンを作成する
    def createAuthToken(self, user:M_User):
        #ユーザートークンIDをユーザーマスタに反映させる
        token:T_UserToken = T_UserToken().create_token(user=user)
        #ユーザーマスタにユーザートークンを保存する
        user.UserTokenId = token
        user.save()
        return token

