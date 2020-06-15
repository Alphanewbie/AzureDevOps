from django.contrib import admin
# 현재 디렉토리의 model에서(.model) Article를 import 하겠다.
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin) :
    # list_display를 상속한다.
    # 테이블을 바로 보여 준다.
    list_display = ['pk','title','contetn']
    # 테이블을 바로 수정할 수 있게 한다.
    list_editable = ['title']


# admin 에 등록해야 한다.
# 위에 클래스를 작성 하고, ArticleAdmin또한 등록한다.
admin.site.register(Article,ArticleAdmin)
