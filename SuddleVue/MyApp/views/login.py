from distributed.protocol.serialize import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json
from MyApp.models import  Book
# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
     response = {}
     try:
         book = Book(book_name=request.GET.get('book_name'))
         book.save()
         response['msg'] = 'success'
         response['error_num'] = 0
     except Exception as e:
         response['msg'] = str(e)
         response['error_num'] = 1
     return JsonResponse(response)



