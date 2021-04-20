from django.core.validators import FileExtensionValidator
from django.db import models

from memFrame.models import T_UserToken

'''
ユーザーモデル
@author Nozawa
'''
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser

# Userクラス
class M_User(AbstractBaseUser, PermissionsMixin):
    #フィールド定義
    id = models.BigAutoField(primary_key=True,unique=True)
    username = models.CharField(max_length=400, unique=True)
    email = models.CharField(max_length=400)
    password = models.CharField(max_length=400)
    role = models.CharField(max_length=400)
    updateDate = models.DateField()
    deleteFlg = models.BooleanField()
    bannedFlg = models.BooleanField()
    UserTokenId = models.ForeignKey(
        T_UserToken.T_UserToken,
        related_name='T_UserToken',
        null=True,
        on_delete=models.CASCADE,  # デフォルト動作指定、UserHogeの削除時にユーザーモデルも削除される
        blank=True
        )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','email']

    def __str__(self):
        return '<User:id' + str(self.id) + ', ' + \
            self.username + ')>'