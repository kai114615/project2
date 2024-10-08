from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import Member
from django.contrib.auth.hashers import make_password

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
    members = Member.objects.all()
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
    # member = Member.objects.get(member_id=28)
    # member.delete()

    # return HttpResponse('資料庫操作練習')
    # 讀取會員所有資料
    # members = Member.objects.all()
    return render(request, 'member/index.html', locals())


def mobile(request):
    return HttpResponse('<h2>Mobile 專屬</h2>')


def register(request):
    if request.method == 'POST':  # 要大寫   #把資料透過body標籤中的封包傳遞
        name = request.POST.get('userid')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')
        birth = request.POST.get('userbirth')

        # 接收上傳的檔案
        avator = request.FILES.get('userphoto')
        # # 檔案名稱
        file_name = avator.name
        # # 檔案大小
        # file_size = avator.size
        # # 檔案類型
        # file_type = avator.content_type

        # print(f'檔案名稱: {file_name}')
        # print(f'檔案大小: {file_size}')
        # print(f'檔案類型: {file_type}')
        # print(email)
        # print(avator)

        # 上傳檔案儲存到 uploads資料夾
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, avator)

        # 將表單傳過來的資料寫近資料庫
        Member.objects.create(
            member_name=name,
            member_password=make_password(password),
            member_birth=birth,
            member_email=email,
            member_avatar=upload_file
        )
        return redirect('member:index')   # 完成註冊後頁面將轉到 /member/ 的index頁面

        # print(f'upload file:{upload_file}')
    return render(request, 'member/register.html')


def edit(request):
    if request.method == 'POST':
        id = request.POST.get('userid')
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        birth = request.POST.get('userbirth')

        # 接收上傳的檔案
        avator = request.FILES.get('userphoto')
        # 檔案名稱
        file_name = avator.name

        # 上傳檔案儲存到 uploads資料夾
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, avator)

        # 修改到資料庫
        member = Member.objects.get(member_id=id)
        member.member_name = name
        member.member_email = email
        member.member_birth = birth
        member.member_avatar = upload_file
        member.save()  # 有修改就要有儲存
        return redirect('member:index')

    id = request.GET.get('id', 30)
    member = Member.objects.get(member_id=id)
    return render(request, 'member/edit.html', locals())


def delete(request, id):
    member = Member.objects.get(member_id=id)
    member.delete()
    return redirect('member:index')
