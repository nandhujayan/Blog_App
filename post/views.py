from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from login.serializer import RegisterSerailizer
from login.models import RegistrationModel
from django.db.models import Q

# Create your views here.


@csrf_exempt
def Post(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check=RegisterSerailizer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Resgistered successful"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed Registration"}))

