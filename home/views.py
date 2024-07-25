from django.shortcuts import render
from .models import Sakila

# Create your views here.


def index(request):
    id = request.GET.get('id', 1)  # 此寫法比較不會爆錯、當掉
    country = ''
    if request.method == 'POST':
        country = request.POST.get('country', '')  # 空字串表示預設不帶出東西

    return render(request, 'home/index.html', {'id': id, 'country': country})


def country(request):
    country = Sakila.country()
    # print(country)
    return render(request, 'home/country.html', {'country': country})


def categories(request):
    categories = Sakila.categories()
    return render(request, 'home/categories.html', {'categories': categories})


def cities(request):
    # print(request.Get['id'])
    id = request.GET.get('id', 1)
    country = request.GET.get('country', '')
    cities = Sakila.cities(id)
    print(cities)
    return render(request, 'home/cities.html', {'cities': cities, 'country': country})
