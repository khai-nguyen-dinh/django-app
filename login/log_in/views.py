from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request

from log_in.models import user


def sign_in(request):
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)
    if username :
        if password:
            request.session['username'] = username
            request.session['password'] = password
    username = request.session.get('username',None)
    password = request.session.get('password',None)
    temp = user(password = password, username = username)
    if temp:
        return render(request,'log_in/index.html',{'temp' : temp})
    else:
        return render(request,'log_in/index.html')

def sign_out(request):
    try:
        del request.session['username']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponseRedirect("/log_in/sign_in/")
