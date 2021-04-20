from django.shortcuts import render
from django.views.generic import TemplateView
'''
Welcomeページのビュー
@author Nozawa
'''
class WelcomeView(TemplateView):
    template_name = 'memFrame/Welcome.html'
    def __init__(self):
        self.params = {
            'title': 'Hello!'
        }

    def get(self, request):
        #カラムを指定して取り出す
        return render(request, 'memFrame/Welcome.html', self.params)