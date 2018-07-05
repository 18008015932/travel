

import random
import time

from datetime import timedelta, datetime
from django.shortcuts import render

from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponseRedirect
# Create your views here.
from user.models import User,UserTicket


def home(request):
    if request.method == 'GET':

        return render(request, 'home.html')


def article(request):
    if request.method == 'GET':
        return render(request, 'article.html')


def detail(request):
    if request.method == 'GET':
        return render(request, 'detail.html')


def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')


def resource(request):
    if request.method == 'GET':
        return render(request, 'resource.html')



def user_register(request):

    if request.method == 'GET':

        return render(request,'register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        email = request.POST.get('email')

        password = make_password(password)
        User.objects.create(
            username=username,
            password=password,
            tel=tel,
            email=email
        )

        return render(request,'login.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        tel = request.POST.get('tel')
        password = request.POST.get('password')
        if User.objects.filter(tel=tel).exists():
            user = User.objects.get(tel=tel)
            if check_password(password,user.password):
                ticket = ''
                s = '1234567890qwertyuiopasdfghjklzxcvbnm'
                for _ in range(15):
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK_' + ticket + str(now_time)
                response = HttpResponseRedirect('/user/home/')
                out_time = datetime.now() + timedelta(days=1)
                response.set_cookie('ticket',ticket,expires=out_time)
                UserTicket.objects.create(ticket=ticket,out_time=out_time,name_id=user.userid)

                user.save()
                return response
            else:
                return render(request, 'login.html', {'password': '用户密码错误'})

        else:
            return render(request, 'login.html', {'tel': '用户不存在'})

def logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect('/index/index/')
        response.delete_cookie('ticket')
        ticket = request.COOKIES.get('ticket')
        UserTicket.objects.filter(ticket=ticket).delete()
        return response