from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader

import json

# Create your views here.


#convert to the login site
def login(request):
    template = loader.get_template('users/login.html')
    content = {
    }
    return HttpResponse(template.render(content,request))


#verify user
def verify_user(request):
    user =  authenticate(username = request.POST['username'], password = request.POST['password'])
    if user is not None:
        return HttpResponse(json.dumps({
            "status" : "success",
        }))
    else:
        return HttpResponse(json.dumps({
            "status" : "fail"
        }))
