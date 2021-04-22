"""config URL Configuration

The `urlpatterns` list routes URLs to viewsTemplate. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function viewsTemplate
    1. Add an import:  from my_app import viewsTemplate
    2. Add a URL to urlpatterns:  path('', viewsTemplate.home, name='home')
Class-based viewsTemplate
    1. Add an import:  from other_app.viewsTemplate import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from memFrame.viewsTemplate.HomeView import HomeView
from memFrame.viewsTemplate.WelcomeView import WelcomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view(), name='Welcome'),
    path('home/', HomeView.as_view(), name='Home'),
    path('account/', include('memFrame.urlrouting.authenticate_routing')),
    path('picture/', include('memFrame.urlrouting.pict_routing')),

#画像ファイル設定
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)