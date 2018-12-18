
from django.shortcuts import render, render_to_response,redirect
from .models import User
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# 显示注册页面
def res(request):
    try:
        del request.session['error']
    except:
        return render(request, 'res.html')
    return render(request, 'res.html')


# 注册操作
def do_res(request):
    stuid = request.POST.get('stuid')
    if not User.objects.filter(stuid=stuid):
        password = request.POST.get('password')
        username = request.POST.get('username')
        tele = request.POST.get('tele')
        class1 =request.POST.get('class1')
        major =request.POST.get('major')
        sex = request.POST.get('sex')
        User.objects.create(stuid=stuid,password=password,username=username,tele=tele,class1=class1,major=major,sex=sex)
        return redirect(reverse('login_res:login'))  # 注册成功，重定向到登录页面
    else:
        request.session['error'] = '用户已存在'
        con = {
            'stuid': request.POST.get('stuid'),
            'password': request.POST.get('password'),
        }
        return render(request, 'res.html', con)



class UserForm(forms.Form):
    stuid = forms.CharField(label = '账号 :',max_length = 15)
    password = forms.CharField(label = '密码 :',widget = forms.PasswordInput())

def login(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            stuid = uf.cleaned_data['stuid']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(stuid__exact = stuid,password__exact = password)
            if user:
                request.session['stuid'] =stuid
                return render_to_response('sells/product/home.html', {'stuid': stuid})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})