from django.db import models

'''
ユーザーモデル
@author Nozawa
'''

# Userクラス
class T_UserTokenDto():
    id:int
    AuthenticateToken:str
    role:str
    applyDateStart:str
    applyDateEnd:str