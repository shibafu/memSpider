from django import forms

'''
ユーザー登録用モデルフォーム
@author Nozawa
'''
class PictUploadForm(forms.Form):
    name = forms.CharField(max_length=256)
    image = forms.FileField()

    # クラスを適用する
    def __init__(self):
        super().__init__()
        #ユーザー名をCSSで就職
        self.fields['name'].widget.attrs["class"] = "inputtext withicon icon_user"
        self.fields['name'].widget.attrs["placeholder"] = "Title"
        #パスワードをCSSで就職
        self.fields['image'].widget.attrs["class"] = "inputtext withicon icon_picture"
        self.fields['image'].widget.attrs["placeholder"] = "Picture"