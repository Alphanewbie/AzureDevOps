# 관리자 계정 만들기
- 계정 또한 데이터이기 때문에 반드시 migrate 작업 후에 관리자 계정을 생성해야 한다.

## Admin 작성 순서
1. `python manage.py createsuperuser`
    - 사용자 이름 : 
    - 이메일 주소
    - 비밀번호 
    - 차례로 입력(임시로 admin, ,kbk1234로 했다.)

2. `http://127.0.0.1:8000/admin`으로 들어가서 로그인 한다.
    - 확인해 본다.
3. articles에 `admin.py`
```python
# 아티클즈에서 현재 디렉토리의 model을 등록하겠다.
from .models import Article

# admin 에 등록해야 한다.
admin.site.register(Article)
```
- 바뀐거 구경하러 간다.
    ### 추가 사항
    1. ArticleAdmin을 등록해 본다.
    ```python
    from .models import Article

    # Register your models here.
    class ArticleAdmin(admin.ModelAdmin) :
        # list_display를 상속한다.
        list_display = ['pk','title','contetn']


    # admin 에 등록해야 한다.
    # 위에 클래스를 작성 하고, ArticleAdmin또한 등록한다.
    admin.site.register(Article,ArticleAdmin)
    ```

    ``` python
    # 테이블을 바로 보여 준다.
    list_display = ['pk','title','contetn']
    # 바로 수정 가능하게 한다
    list_editable = ['title']
    ```
