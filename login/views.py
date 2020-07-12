from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from . import models
from . import forms
import hashlib


def hash_code(s, salt='myblog'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):   # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():             # 确保用户名和密码都不为空
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(user_name=username)
            except Exception:
                message = '用户不存在'
                return render(request, 'login/login.html', locals())
            if user.password == hash_code(password):
                # 通过下面的语句，往session字典内写入用户状态和数据
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.user_name
                return redirect('/index/', )
            else:
                message = '密码不正确'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        redirect('/index/')
    if request.method == "POST":
        register_form = forms.RegistryFrorm(request.POST)
        message = '请检查填写的内容'
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            if password1 != password2:
                message = '两次输入的密码不一致'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(user_name=username)
                if same_name_user == username:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册'
                    return render(request, 'login/register.html', locals())
                new_user = models.User()
                new_user.user_name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
        return redirect(request, 'login/register.html', locals())
    register_form = forms.RegistryFrorm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect(request, '/login/')

