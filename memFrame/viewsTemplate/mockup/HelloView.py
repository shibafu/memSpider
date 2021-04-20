from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from memFrame.forms import HelloForm
'''
HelloPageのビュークラスです
@author Nozawa
'''
class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello!',
            'message': 'your data',
            'form': HelloForm.HelloForm(),
            'data':[]
        }

    #def get(self, request):
    #    #カラムを指定して取り出す
    #    #params['data'] = Friend.objects.all().values_list('id', 'name', 'mail')
    #    self.params['data'] = Friend.objects.all()
    #    return render(request, 'memFrame/mock_index.html', self.params)
    
    def post(self, request):

        params = {
            'title':'Hello!WelcomePage',
            'msg':'これはサンプルで作ったページです',
            'form' : HelloForm.HelloForm(),
            'data':[]
        }
        #num = request.POST['id']
        #item = Friend.objects.get(id=num)
        #params['data'] = [item]
        #params['form'] = HelloForm.HelloForm(request.POST)

        #self.params['form'] = HelloForm.HelloForm(request.POST)

        #return render(request, 'memFrame/mock_index.html', self.params)