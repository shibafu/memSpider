from django import forms

'''
ユーザー登録用モデルフォーム
@author Nozawa
'''
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.CharField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=200)

    # クラスを適用する
    def __init__(self):
        super().__init__()
        #ユーザー名をCSSで就職
        self.fields['username'].widget.attrs["class"] = "inputtext withicon icon_user"
        self.fields['username'].widget.attrs["placeholder"] = "Username"
        #EMailをCSSで就職
        self.fields['email'].widget.attrs["class"] = "inputtext  withicon icon_email"
        self.fields['email'].widget.attrs["placeholder"] = "MailAddress"
        #パスワードをCSSで就職
        self.fields['password'].widget.attrs["class"] = "inputtext withicon icon_password"
        self.fields['password'].widget.attrs["placeholder"] = "Password"