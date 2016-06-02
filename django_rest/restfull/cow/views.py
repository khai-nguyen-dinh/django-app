from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from cow.models import Post,User
from cow.serializes import UserSerialize,PostSerialize
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

@csrf_exempt

def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerialize(user,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = UserSerialize(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = UserSerialize(user)
        return JSONResponse(serializer.data)
    if request.method == 'PUSH':
        data = JSONParser().parse(request)
        serializer = UserSerialize(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
