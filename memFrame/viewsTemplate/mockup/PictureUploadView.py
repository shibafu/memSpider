from django.shortcuts import render
from django.views.generic import TemplateView

from memFrame.service import PictService
from memFrame.ModelForm import mock_PictUploadForm

'''
画像アップロードビューです
@author Nozawa
'''


class PictureUploadView(TemplateView):
    #画像サービスクラス
    pictService:PictService = PictService.PictService()
    #初期化処理
    def __init__(self):
        self.params = {
            'form': mock_PictUploadForm.PictUploadForm(),
        }
    # 画像フォームを表示する
    def get(self, request):
        # 画像オブジェクトを代入
        return render(request, 'memFrame/mock_pictUpload.html', self.params)

    # 画像フォームを表示する
    def post(self, request):
        self.pictService.createFromRequest(request)

        # 画像オブジェクトを代入
        self.params['resultMessage'] = "登録処理が完了しました！"
        return render(request, 'memFrame/mock_pictUpload.html', self.params)