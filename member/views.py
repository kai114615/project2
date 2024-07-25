from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    html = '<h2>Hello Django</h2>'
    # print(request.headers.get('content-type'))
    # print(request.headers.get('user-agent'))

    # html += '<ul>'
    # for key, value in request.headers.items():
    #     html += f'<li>{key}:{value}</li>'
    # html += '</ul>'
    # return HttpResponse(html)


    # user_agent = request.headers.get('user-agent')
    # if 'Mobile' in user_agent:
    #     return redirect('/member/mobile/')

    # print(request.method)

    name = request.GET.get('username')  #網址後面?key=value的東西傳遞
    if name is None:
        name = 'django'
    html = f'<h2>Hello {name}</h2>'

    response = HttpResponse(html)
    response.status_code = 200

    return HttpResponse(html)
    # return render(request, 'member/index.html')


def mobile(request):
    return HttpResponse('<h2>Mobile 專屬</h2>')

def register(request):
    if request.method == 'POST':  #要大寫   #把資料透過body標籤中的封包傳遞
        name = request.POST.get('username')
        email = request.POST.get('useremail')

        # 接收上傳的檔案
        avator = request.FILES.get('avator')
        # 檔案名稱
        file_name = avator.name
        # 檔案大小
        file_size = avator.size
        # 檔案類型
        file_type = avator.content_type

        print(f'檔案名稱: {file_name}')
        print(f'檔案大小: {file_size}')
        print(f'檔案類型: {file_type}')
        # print(email)
        # print(avator)

        # 上傳檔案
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, avator)
        print(f'upload file:{upload_file}')

    return render(request, 'member/register.html')
