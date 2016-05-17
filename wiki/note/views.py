from django.utils import timezone

from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post


# Create your views here.
def index(request):
    id = request.session.get('id', None)
    if id:
        return HttpResponseRedirect('/note/main/')
    return render(request,'note/index.html')
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
            return HttpResponseRedirect('/note/index/')
    else:
        return render(request, 'note/signup.html')


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    users = User.objects.all()
    if username or password:
        for x in users:
            if x.username == username and x.password == password:
                request.session['id'] = x.id
                return HttpResponseRedirect('/note/main/')

        return render(request, 'note/login.html', {'error': 'sai ten tai khoan hoac mat khau!'})
    else:

        return render(request, 'note/login.html')


@csrf_exempt
def main(request):
    content = request.POST.get('content', None)
    title = request.POST.get('title', None)
    posted = timezone.now()
    id = request.session.get('id', None)
    user = User.objects.get(id=id)
    if title or content:
        user.post_set.create(title=title, content=content, posted=posted)
        post = user.post_set.all()
        return render(request, 'note/post.html', {'post': post})
    post = user.post_set.all()
    return render(request, 'note/post.html', {'post': post})

@csrf_exempt
def edit(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            post = Post.objects.get(id=id)
            return render(request, 'note/edit.html', {'post': post})
        else:
            return HttpResponseNotFound('<h1>Page not found</h1>')

    if request.method == 'POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        id = request.POST.get('id', None)
        post = Post.objects.get(id=id)
        if title or content:
            post.title = title
            post.content = content
            post.save()
            return HttpResponseRedirect('/note/main')
        return render(request, 'note/edit.html', {'error': 'error:no data!'})


@csrf_exempt
def delete(request):
    id = request.GET.get('id', None)
    if id:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect('/note/main')

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def logout(request):
    del request.session['id']
    return HttpResponseRedirect('/note/')