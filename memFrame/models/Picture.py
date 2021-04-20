from django.core.validators import FileExtensionValidator
from django.db import models

'''
画像モデル
@author Nozawa
'''
class Picture(models.Model):
    id = models.BigAutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='upload_pict/%Y/%m/%d/',
                             verbose_name='アップロード画像',
                             validators=[FileExtensionValidator(['jpg','png','gif', ])],
                             )
    uploader = models.CharField(max_length=200)
    uploadDate = models.DateField()
    updateDate = models.DateField()
    deleteFlg = models.BooleanField()

    def __str__(self):
        return '<Picture:id' + str(self.id) + ', ' + \
            self.name + '(' + str(self.uploader) + ')>'