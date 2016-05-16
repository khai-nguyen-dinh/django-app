import re

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from django.template.context import Context
from django.views.decorators.csrf import csrf_exempt

from vi.models import Post


@csrf_exempt
def index(request,title=""):

    if title :
        post = Post.objects.filter(title=title)
        if post:
            return process('vi/page.html', post[0])
        else:
            return render(request,'vi/edit.html', {'post': title})
    else:

        page = Post.objects.get(title='test')
        return process('vi/page.html', page)

@csrf_exempt
def edit(request, title):
    page = Post.objects.get(title=title)
    return render(request,'vi/edit.html', {'title':title, 'content':page.content})


@csrf_exempt
def save(request, title):
    content = request.POST['content']
    pages = Post.objects.filter(title=title)
    if pages:
        pages[0].content = content
        pages[0].save()
    else:
        page = Post(title=title, content=content)
        page.save()
    return HttpResponseRedirect("/vi/%s/" % title)

r = re.compile(r'\b(([A-Z]+[a-z]+){2,})\b')

def process(template, post):
    t = loader.get_template(template)
    content = r.sub(r'<a href="/vi/\1">\1</a>', post.content)
    content = re.sub(r'[\n\r]+', '<br>', content)
    c = Context({'title':post.title,'content':content})
    return HttpResponse(t.render(c))

