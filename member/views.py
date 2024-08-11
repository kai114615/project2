from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import Member

# Create your views here.


def index(request):
    # html = '<h2>Hello Django</h2>'
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

    # name = request.GET.get('username')  #網址後面?key=value的東西傳遞
    # if name is None:
    #     name = 'django'
    # html = f'<h2>Hello {name}</h2>'

    # response = HttpResponse(html)
    # response.status_code = 200

    # return HttpResponse(html)
    # return render(request, 'member/index.html')

    # 資料庫的操作
    # 新增
    # Member.objects.create(
    #     member_name = 'jhgfdsfg',
    #     member_password = '12345',
    #     member_birth = '1993-4-17',
    #     member_email = '75242@gmail.com'
    # )

    # 讀取所有會員資料
    # members = Member.objects.all()
    # print(members)

    # # 讀取單筆資料
    # member = Member.objects.get(member_id=4)
    # print(member)

    # 修改
    # member = Member.objects.get(member_id =14)  # 指定修改哪一筆資料
    # member.member_name = 'tony'
    # member.member_birth = '1987-12-24'
    # member.save()  # 有修改就要有儲存

    # 刪除
    # member = Member.objects.get(member_id=14)
    # member.delete()

    return HttpResponse('資料庫操作練習')


def mobile(request):
    return HttpResponse('<h2>Mobile 專屬</h2>')


def register(request):
    if request.method == 'POST':  # 要大寫   #把資料透過body標籤中的封包傳遞
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')
        birth = request.POST.get('userbirth')

        # 將表單傳過來的資料寫近資料庫
        Member.objects.create(
            member_name = name,
            member_password = password,
            member_birth = birth,
            member_email = email
        )

        # 接收上傳的檔案
        avator = request.FILES.get('userphoto')
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
