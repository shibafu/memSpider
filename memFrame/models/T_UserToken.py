import hashlib

from django.core.validators import FileExtensionValidator
from django.db import models
from datetime import datetime, timedelta

from config import settings
from memFrame.models import M_User

'''
ユーザーモデル
@author Nozawa
'''
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser

# Userクラス
class T_UserToken(models.Model):
    # ハッシュ作成
    def create_token(self, user:M_User):
        # ハッシュを生成する
        hashInstance = hashlib.sha3_512()
        hashInstance.update(str(datetime.now().strftime('%Y/%m/%d %H:%M*%S') + user.password).encode('UTF-8'))
        self.AuthenticateToken = hashInstance.digest()
        #ロール
        self.role = user.role
        #適用開始日付を設定
        self.applyDateStart = datetime.now()
        #適用終了日付を設定
        #開始日付+30日
        self.applyDateEnd = datetime.now() + timedelta(days=30)
        #DBに登録
        self.save()
        #オブジェクトを返す
        return self

    #フィールド定義
    id = models.BigAutoField(primary_key=True,unique=True)
    # ユーザーモデルと外部キーを構成する
    AuthenticateToken = models.CharField(max_length=400)
    role = models.CharField(max_length=400)
    applyDateStart = models.DateTimeField
    applyDateEnd = models.DateTimeField()
    def str (self):
        return '<User:id' + str(self.id) + ', ' + ')>'