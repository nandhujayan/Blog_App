from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from post.serializer import PostSerailizer
from post.models import PostModel
from django.db.models import Q

# Create your views here.


@csrf_exempt
def AddPost(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check=PostSerailizer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"new Post  added success"}))
        else:
            return HttpResponse(json.dumps({"status":"Post addedFailed"}))


@csrf_exempt
def viewAll(request):
    if request.method=="POST":
        postlist=PostModel.objects.all()
        serialize_data=PostSerailizer(postlist,many=True)
        return HttpResponse(json.dumps(serialize_data.data))
    