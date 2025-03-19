from gc import get_objects

from django.http import HttpResponse
from django.shortcuts import render
from bookmark.models import Bookmark
# from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.

def bookmark_list(request):
    # bookmarks = Bookmark.objects.all() 19강에선 적용안함
    # SELECT * FROM bookmark
    bookmarks = Bookmark.objects.filter(id__gt=117)
    context = {
        'bookmarks': bookmarks,
    }

    # return HttpResponse("<h1>북마크 리스트 페이지 입니다.</h1>")
    return render(request, 'bookmark_list.html', context)

def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(id=pk)
    # except:
    #     raise Http404

    bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {'bookmark': bookmark}
    return render(request, 'bookmark_detail.html', context)
