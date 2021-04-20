from django import forms

'''
ユーザー登録用モデルフォーム
@author Nozawa
'''
class SignInForm(forms.Form):
    name_or_mail = forms.CharField(max_length=200)
    email = forms.CharField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=200)

    # クラスを適用する
    def __init__(self):
        super().__init__()
        #ユーザー名をCSSで就職
        self.fields['name_or_mail'].widget.attrs["class"] = "inputtext withicon icon_user"
        self.fields['name_or_mail'].widget.attrs["placeholder"] = "Username"
        #パスワードをCSSで就職
        self.fields['password'].widget.attrs["class"] = "inputtext withicon icon_password"
        self.fields['password'].widget.attrs["placeholder"] = "Password"