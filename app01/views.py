from django.shortcuts import render,HttpResponse

# Create your views here.
from rabc.models import *


def users(request):
    user_list = User.objects.all()
    # permission_list = request.session.get('permission_list')
    # print(permission_list)

    # 查询当前用户如的名字 把名字显示在右上角
    id = request.session.get('user_id')
    user = User.objects.filter(pk=id).first()


    return render(request,'users.html',locals())

import re
def add_user(request):
    # 中间件service rabc帮你校验 在通关条件return none 跳出中间件 来到每个函数
    return HttpResponse('add user...........')
    # permission_list = request.session['permission_list']
    # current_path = request.path_info
    # # if current_path in permission_list: 不能这么写 因为列表里编辑删除的URL是正则匹配的 直接in 定死了
    #
    # for permission in permission_list:
    #     permission = '^%s$'%permission
    #     print(permission)
    #     ret =re.match(permission,current_path)
    #     print(ret)
    #     if ret:
    #         return HttpResponse('add user...........')
    #
    # return HttpResponse('你没有访问权限')


def del_user(request,id):
    return HttpResponse('del'+id)


def roles(request):
    role_list = Role.objects.all()
    # permission_list = request.session['permission_list']
    # current_path = request.path_info
    # for permission in permission_list:
    #     permission = '^%s$'%permission
    #     ret = re.match(permission,current_path)
    #     if ret:
    #         return render(request,'roles.html',locals())
    # return HttpResponse('没有权限')
    return render(request, 'roles.html', locals())




from rabc.service.permissions import *
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=user,pwd=pwd).first()
        if user:
            #  在session中 注册用户ID 这是用户信息

            request.session['user_id'] = user.pk



            # 注册当前用户的所有权限到session中
            # ret = user.roles.all() #  拿到用户角色
            #print(ret)  #   <QuerySet [<Role: 保洁>, <Role: 销售>]>
            initial_session(user, request) # user是User对象



            return HttpResponse('登录成功')
    # 没登录成功 调回登录页面
    return render(request,'login.html')