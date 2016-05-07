from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from vi.models import Post


@csrf_exempt
def index(request,title=""):
    if title :
        title = Post.objects.filter(title=title)
        if title:
            return render(request,('vi/'))

