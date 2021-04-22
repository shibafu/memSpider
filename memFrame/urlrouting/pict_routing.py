"""django_app URL Configuration
画像関係ののURL定義
"""
from django.urls import path

from memFrame.viewsTemplate.PictUploadView import PictUploadView
from memFrame.viewsTemplate.mockup.PictureUploadView import PictureUploadView

urlpatterns = [
    path('PictUpload', PictUploadView.as_view(), name='PictUpload'),  # 画像アップロードページ

]