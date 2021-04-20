from django.core.validators import FileExtensionValidator
from django.db import models

from memFrame.models import M_User

'''
画像モデル
@author Nozawa
'''
class T_Picture(models.Model):
    id = models.BigAutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='upload_pict/%Y/%m/%d/',
                             verbose_name='アップロード画像',
                             validators=[FileExtensionValidator(['jpg','png','gif', ])],
                             )

    M_UserId = models.ForeignKey(
        M_User,
        related_name='M_User',
        null=True,
        on_delete=models.CASCADE,  # デフォルト動作指定、UserHogeの削除時にユーザーモデルも削除される
        blank=False
        )
    uploader = models.CharField(max_length=200)
    uploadDate = models.DateField()
    updateDate = models.DateField()
    deleteFlg = models.BooleanField()

    def __str__(self):
        return '<Picture:id' + str(self.id) + ', ' + \
            self.name + '(' + str(self.uploader) + ')>'