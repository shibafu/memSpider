from django.shortcuts import render
from django.views.generic import TemplateView

from memFrame.service import PictService
from memFrame.ModelForm import mock_PictUploadForm

'''
画像の表示ビューです
@author Nozawa
'''


class PictureViewingView(TemplateView):
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
        pictList:list = self.pictService.findAll()
        lists: list = {'aa','bb','awdqa'}
        self.params = {
            'picts':pictList,
            'list':lists,
        }

        print(pictList)

        return render(request, 'memFrame/mock_pictViewingView.html', self.params)