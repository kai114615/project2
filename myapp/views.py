from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse('<h2>Myapp 首頁</h2>')
    store_title = '商城首頁'
    now = datetime.now()
    id = 'kuytrhgefsadfhnfnhmjuiyktrjhesfdghcfuytdref'
    value1 = ['123', ['456', '789', ['01112', '131415', '161718']], '192021']

    # locals功能可將參數自動整理成{dict}的形式來呈現
    return render(request, 'myapp/index.html', locals())  

def about(request, year=datetime.now().year):
    return HttpResponse(f'<h2>About {year} </h2>')

def details(request, product_id=''):
    return HttpResponse('<h2>讀出商品編號{product_id}的商品</h2>')

def blog(request, publish=None):
    return HttpResponse(f'<h2>讀取{publish}的文章</h2>')

def course(request, course_name=None):
    return HttpResponse(f'<h2>課程名稱：{course_name}</h2>')

def show(request):
    return render(request, 'myapp/show.html', {'title':'store show'})