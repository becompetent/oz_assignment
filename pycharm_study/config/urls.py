"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404
from django.shortcuts import render
from bookmark import views

movie_list = [
    {'title': '파묘', 'director': '장재현'},
    {'title': '웡카', 'director': '폴 킹'},
    {'title': '듄: 파트 2', 'director': '드니 빌뇌브'},
    {'title': '시민덕희', 'director': '박영주'},
]

# book_list = [
#     {'title': '해커스 토익 기출 VOCA', 'writer': 'David cho 해커스어학연구소', 'genre': '자격증'},
#     {'title': '모순', 'writer': '양귀자 쓰다', 'genre': '한국소설'},
#     {'title': '스토너', 'writer': '존 윌리엄스 알에에치 코리아', 'genre': '영미소설'},
#     {'title': '초역 부처의 말', 'writer': '코이케류노스케', 'genre':'인문교양'},
# ]
def index(request):
    return HttpResponse("<h1>hello</h1>")


def book_list(request):
    # book_text = ''
    #
    # for i in range(0, 4):
    #     book_text += f'book {i}<br>'
    return render(request, 'book_list.html', {'range': range(1, 10)})

def book(request, num):
        return  render(request, 'book_detail.html', {'num': num})


def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지 입니다.</h1>')

def movies(request):
    #movie_titles = [movie['title'] for movie in movie_list]
    #
    # 같은 함수 movie_title = [
    #     f'<a href="/movie/{index}/">{movie["title"]}</a>'
    #     for index, movie in enumerate(movie_list):
    #]
#     #for 문으로 작성시
#     # movie_titles = []
#     # for movie in movie_list:
#     #    movie_titles.append(movie['title'])
#
#     response_text = ''
#
#     for index, title in enumerate(movie_titles):
#         response_text += f'<a href="/movie/{index}/">{title}</a><br>'
#
#     return HttpResponse(response_text)
    return render(request, 'movies.html', {'movie_list': movie_list})

def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404

    movie = movie_list[index]
    # context = {'movie': movie}
    # return render(request, 'movie.html', context)
    return render(request, 'movie.html', {'movie': movie})

def gugu(request, num):
    context = {
        'num': num,
        'results': [num * i for i in range(1, 10) ]
    #     'range': range(1, 10),
    }
    return render(request, 'gugu.html', context)



urlpatterns = [
    path("admin/", admin.site.urls),
#     path('', index),
#     path('book_list/', book_list),
#     path('book_list/<int:num>/', book),
#     path('language/<str:lang>/', language),    #str 아래에 글자들어가는 함수 쓰면 str에서 먼저 실행되서 적용되지 않을 수 있는 점 유의
#     path('movie/', movies),
#     path('movie/<int:index>/', movie_detail),
#     path('gugu/<int:num>/', gugu),
    path('bookmark/', views.bookmark_list),
    path('bookmark/<int:pk>/', views.bookmark_detail),
]
