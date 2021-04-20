from django import forms
from django.contrib.auth.models import User

from memFrame.models.Picture import Picture

'''
ユーザー登録用モデルフォーム
@author Nozawa
'''
class UserUploadForm(forms.Form):
    username = forms.CharField(label='name', required=True)
    email = forms.EmailField(label='email', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)