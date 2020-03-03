from distributed.protocol.serialize import serializers
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from MyApp import models
def getpic(request):
    response={}
    response['data'] = []
    if request.method == "GET":
        allimg = models.Img.objects.all()
        for im in allimg:
            response['data'].append(
                {
                    "id":im.id,
                    'img': im.imgpic,
                }
            )
            response['img']='success'
            response['code']=200
        return JsonResponse(response)


