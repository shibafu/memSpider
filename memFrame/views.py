from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) :

    params = {
        'title':'Hello!WelcomePage',
        'msg':'これはサンプルで作ったページです'
    }

    return render(request, 'memFrame/index.html', params)



def next(request) :

    params = {
        'title':'nextPage',
        'msg':'リンク先のページです'
    }

    return render(request, 'memFrame/index.html', params)


