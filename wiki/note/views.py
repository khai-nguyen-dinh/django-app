from datetime import timezone

from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post


# Create your views here.
@csrf_exempt
def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    user = User(username=username, password=password, email=email)
    users = User.objects.all()

    if username and password and email:
        if any(x.email == email for x in users):
            return render(request, 'note/signup.html', {'error': 'error'})
        else:
            user.save()
            return HttpResponseRedirect('/note/login/')
    else:
        return render(request, 'note/signup.html')

@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    users = User.objects.all()
    if username or password:
        for x in users:
            if x.username == username and x.password == password :
                request.session['id'] = x.id
                return HttpResponseRedirect('/note/main/')

        return render(request,'note/login.html',{'error' : 'sai ten tai khoan hoac mat khau!'})
    else:

        return render(request,'note/login.html',{'error' : 'ban chua nhap du du lieu'})

def main(request):
    content = request.POST.get('content',None)
    title = request.POST.get('title',None)
    posted = timezone.now()
    id = request.session.get('id', None)
    user = User.objects.get(id)
    if title or content:
        post = user.user_set.all()
        return render(request,'note/post.html',{'post' : post})
    post = Post(id,title,content,posted)
    post.save()
    post = user.user_set.all()
    return render(request, 'note/post.html', {'post': post})

def edit(request,post):
    if request.method == 'POST':
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        if title or content:
            return render(request,'note/edit.html',{'error': 'error:no data!'})
        post.title = title
        post.conent = content
        post.save()
        return HttpResponseRedirect('note/main')
    return render(request,'note/edit.html',{'post': post})

def delete(request,post):
    post.delete()
    return HttpResponseRedirect('note/main')
