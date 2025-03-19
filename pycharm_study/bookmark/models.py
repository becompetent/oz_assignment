from django.db import models

# Create your models here.
# model = DB의 (테이블)
# Field = DB의 컬럼

# 북마크
# 이름 => VARCHAR
# URL 주소 => VARCHAR

class Bookmark(models.Model):
    name = models.CharField('이름', max_length=100)
    url = models.URLField('URL')
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정일시', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'

# class BookmarkCategory(models.Model):
# makemigrations ==> migration.py 파일을 만든다. 실제 DB에는 영향이 없음
# => 다만 실제 DB에 넣기 위한 정의를 하는 파일을 생성

# migrate => migrations/ 폴더 안에 있는 migration 파일들을 실제 DB에 적용을 합니다.

# makemigrations => 깃의 커밋 => github에 적용 X, 커밋 기록 => DB에 적용 X, 적용할 파일 생성
# migrate => git 의 push => github에 적용 O, 로컬에 있는 커밋 기록
# => DB에 적용 O, migrations 파일들 가지고 적용


