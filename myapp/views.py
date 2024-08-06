from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Category

# Create your views here.


def index(request):
    # return HttpResponse('<h2>Myapp 首頁</h2>')
    store_title = '商城首頁hello django'
    now = datetime.now()
    id = 'kuytrhgefsadfhnfnhmjuiyktrjhesfdghcfuytdref'
    value1 = ['123', ['456', '789', ['01112', '131415', '161718']], '192021']

    # locals功能可將參數自動整理成{dict}的形式來呈現
    return render(request, 'myapp/index.html', locals())


def about(request, year=datetime.now().year):
    # return HttpResponse(f'<h2>About {year} </h2>')
    return render(request, 'myapp/about.html', {'year': year})


def details(request, product_id=''):
    return HttpResponse(f'<h2>讀出商品編號{product_id}的商品</h2>')


def blog(request, publish=None):
    return HttpResponse(f'<h2>讀取{publish}的文章</h2>')


def course(request, course_name=None):
    return HttpResponse(f'<h2>課程名稱：{course_name}</h2>')


def show(request):
    title = '資料庫讀取'
    # 跟 Model 要資料
    categories = Category.all()
    # print(categories)

    # 把資料傳給 template {}，透過 render() 的第三個參數，傳入一個{} 結構的資料
    return render(request, 'myapp/show.html', locals())


def abc(request):
    user = {'name': 'Jack', 'age': 46}
    users = [{'name': 'Jack', 'email': 'fghtjukjhfhgsd@gmail.com', 'age': 23},
             {'name': 'Patrick', 'email': '34567uhgfdsasdfvg@gmail.com', 'age': 19},
             {'name': 'Sean', 'email': 'sdfg789fghnj0987xdcv23wedf7uh@gmail.com', 'age': 28}]
    title = 'Template 練習'
    return render(request, 'myapp/abc.html', locals())
