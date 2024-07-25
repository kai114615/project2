from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse('<h2>Myapp 首頁</h2>')

def about(request, year=datetime.now().year):
    return HttpResponse(f'<h2>About {year} </h2>')

def details(request, product_id=''):
    return HttpResponse('<h2>讀出商品編號{product_id}的商品</h2>')