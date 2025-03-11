from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bookmark_list(request):
    return HttpResponse("<h1>북마크 리스트 페이지 입니다.</h1>")
