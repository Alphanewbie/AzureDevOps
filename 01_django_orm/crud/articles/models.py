from django.db import models

# Create your models here.
class Article(models.Model):
    # 이 컬렌의 데이터의 길이는 최대 20글자
    # 필수 인자가 필요하다.
    title = models.CharField(max_length = 20)
    # 최대 길이가 존재하지 않는 칼럼
    # 필수 인자가 없다.
    content = models.TextField()
    # auto_now_add 데이터베이스가 최초 생성 일자
    # django ORM이 최소 Insert 시에만 현재 날짜와 시간으로 갱신
    creted_at = models.DateTimeField(auto_now_add=True)
    # 마지막 업데이트 시간으로 갱신한다.
    upated_at = models.DateTimeField(auto_now=True)