from django.shortcuts import render
from django.http import HttpResponse
import json

def restful_demo(request, key):
    result = key
    return HttpResponse(json.dumps({
        "status": "fuck you ",
        "result": result
    }))

def json_display_demo(request):
    list = ["json1", "json2", "fuck you"]
    return HttpResponse(json.dumps({
        "status": "fuckyou status",
        "result": "some kind of result"
    }))

def json_display_demo_1(request):
    list = ["json1", "json2", "fuck you"]
    return HttpResponse(json.dumps({
        "id": "id",
        "password": "pwd"
    }))

def login_request_handler(request):
    login_data = request.POST.get("username","password")
    content = {login_data}
    return_json = {"success": "TRUE"}
    return HttpResponse(json.dumps({
      "success": "TRUE"
    }), content_type="application/json")


def PHGuidings_request_handler(request):
    return_json = {
        "departments": [
            {"name": "口腔科", "id": "j921jxk1lalxk2"},
            {"name": "皮肤科", "id": "kekjkjcckek1"},
            {"name": "肛门科", "id": "fejkj21kljkc3"},
            {"name": "内分泌科", "id": "cc234jkjck32"},
            {"name": "手术室", "id": "llpl2lkj34k1jl"},
            {"name": "避孕室", "id": "cjejkcjkkk1"},
            {"name": "瞎JB室", "id": "cck2jk3kk3h54h"}
        ]
    }
    return HttpResponse(json.dumps(return_json,separators=(',',':')), content_type="application/json")

def PHGuiding_withname_request_handler(request):
    return_json = {
        "departmentName": "口腔科",
        "position": "坐落于XXX的一角",
        "usage": "职能用途",
        "description": "简介在这里"
    }
    return HttpResponse(json.dumps(return_json), content_type="application/json")
