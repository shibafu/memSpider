'''
画像関連の処理を行うサービスです
@author Nozawa
'''
from memFrame.ModelForm.mock_PictUploadForm import PictUploadForm
from memFrame.models import M_User
from memFrame.models.T_Picture import T_Picture
import datetime

class PictService:

    #　画像を新規追加する(画像アップロードフォーム用）
    def createFromRequest(self, request, user:M_User):
        pictObj = T_Picture()
        pictObj.name = request.POST['name']
        pictObj.uploader = "デフォルトゲストです！"
        pictObj.uploadDate = datetime.datetime.today()
        pictObj.updateDate = datetime.datetime.today()
        pictObj.deleteFlg = False
        pictObj.image = request.FILES['image']
        pictObj.M_UserId = user

        # 値をDBへの登録
        pictObj.save()

    #　画像を新規追加する
    def create(self, name, image, uploader):
        pict:T_Picture = T_Picture()
        pict.name = name
        pict.image = image
        pict.uploader = uploader
        pict.uploadDate = datetime.datetime.today()
        pict.updateDate = datetime.datetime.today()
        pict.deleteFlg = False
        pict.save()

    #　画像を更新する
    def update(self, id, name, image, uploader):
        targetPicture:T_Picture = T_Picture.objects.get(id=id)
        targetPicture.name = name
        targetPicture.image = image
        targetPicture.uploader = uploader
        targetPicture.updateDate = datetime.datetime.today()
        targetPicture.save()

    #　画像を論理削除する
    def logicDelete(self, id):
        targetPicture:T_Picture = T_Picture.objects.get(id=id)
        targetPicture.deleteFlg = True
        targetPicture.save()

    # 　画像を物理削除する
    def physicDelete(self, id):
        targetPicture:T_Picture = T_Picture.objects.get(id=id)
        targetPicture.delete()

    #　idをもとに画像を参照する
    def findById(self, id):
        return T_Picture.objects.get(id=id)

    #　idをもとに画像を参照する
    def findAll(self):
        return T_Picture.objects.all()

    def findByUser(self, user):
        return T_Picture.objects.filter(M_UserId=user)
