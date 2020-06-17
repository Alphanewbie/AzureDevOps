# 장고
https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction
## 장고
- djanggo 프로젝트는 **app들의 집합**이고, 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 app들의 역활
- app은 하나의 역활 및 기능 단위로 쪼개는 것이 일반적
- 작은 규모의 서비스에서는 세부적으로 나누지는 않는다.
- app이름은 **복수형**으로 하는 것이 권장된다
## 작동 방식
![basic-django](./basic-django.png)
## 장고 설치
1. `pip list`로 장고 설치 여부 확인
2. `pip install django==2.1.15`로 설치
   
    - 이 버전을 설치한 이유 : 안정성을 위해 그 윗 버전은 너무 최신 버전이라서 안정정이 아직이래.
3. `pip list`로 장고 설치 여부 확인
4. `django-admin.py startproject [프로젝트이름]`으로 실행.
    
    - 예) `django-admin.py startproject firstapp`
    - 단, 프로젝트 이름은 예약어는 안된다.
        - 예) class, test, django..., django-test(하이픈도 사용 금지)
    - 이때만 `djanggo-admin.py` 명령어를 사용한다.
5. 생성된 프로젝트명 디렉토리로 들어간다.
6. `python manage.py runserver`로 장고 서버 실행
   
    - `http://127.0.0.1:8000/`로 들어갔는데 로켓 날아가고 있으면 끝.
7. 생성된 프로젝트 디렉토리에 들어가면  `__init__.py`로 들어가면 비어있는 파일인데, 이건 패키지 파일로 만들어주기 위한 역활
   
    - 나머지 3개는 모듈
8. `python manage.py startapp articles`로 article 을 만든다.
   
    - 하나의 프로젝트는 여러 앱을 가지게 된다.
9. 각각 설명
    - admin.py관리자의 페이지를 수정하는 곳
    - apps 정보가 들어가 있는 곳 절대로 사용하지 않는다.
    - models.py 데이터 베이스,즉 모델을 정의하는 곳
    - test.py 장고의 테스트 케이스를 정의하는 곳
    - views.py 뷰를 정의하는 곳
10. settings.py에 `articles`을 넣어준다.
    ```
    INSTALLED_APPS = [
    'articles',
    # 위에 이것을 넣어준다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]
    ```
    - 장고 앱 넣는 순서.
        1. local apps
        2. third party app
        3. django apps
    - 위에 보면 마지막에,에 있는데 파이선 문법적으로는 틀리지만, 넣는게 장고적 문법

11. 한국으로 세팅
    - `LANGUAGE_CODE = 'en-us'` -> `LANGUAGE_CODE = 'ko-kr'`
    - `TIME_ZONE = 'UTC'` -> `LANGUAGE_CODE = 'Asia/Seoul'`
    - 이러면 어플리케이션이 한번에 앱 전체가 한국으로 세팅된다.

12. urls.py를 확인한다.
    ```
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
    ```
    라고 있는데 `http://127.0.0.1:8000/admin`로 들어간다.
    - 즉, 기본적으로 어드민 페이지가 존재한다.
    `path('index/', ),`와 `from articles import views` 추가한다.
        - 끝에 '/':엔드 슬래시 를 반드시 추가해 줘야한다.
    - 이후에 이런 모습
    ```
    from django.contrib import admin
    from django.urls import path
    from articles import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index),
    ]
    ```
13. 이제 views.py 작성하러 간다.
    ```
    # 리퀘스트는 무슨 뷰던지 간에 반드시 필요
    def index(request) :
        # 첫번째 인자, 리퀘스트
        # 두번째 이름, temple이름
        return render(request,[templesname])
    ```
14. `firstapp/articles/`안에 `templates/` 디렉토리 만든다.
    
    - 반드시 template**s**여야 한다.

----

15. 나중에 app이 너무 많아졌을 때, `python manage.py startapp [새 앱을 만든다.]`
    1.  setting 에 새로운 앱을 등록한다.
    2.  기존에 존재하는 `artilce` 즉, 첫번째 app 디렉토리에 `urls.py`를 새로 생성한다.
    3.  ``` python
            from django.urls import path
            from . import views

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('index/', views.index),
                path('dinner/', views.dinner),
                path('picsum/', views.picsum),
                # 밑에 2개는 같다. str이 디폴트 값이다.
                path('hello/<str:name>/',views.hello),
                path('hello/<name>/',views.hello),
                path('hello/<str:name>/<int:age>/',views.iam),
                path('multi/<int:num1>/<int:num2>/',views.multi),
                path('dtl',views.dtl_practice),
                path('palindrome/<str:word>',views.palindrome),
                path('throw',views.throw),
                path('catch/',views.catch),
                path('lotto/',views.randomnum),
            ]
        ```
    4. 기존에 존재하던 `from django.urls import path`에 include를 붙힌다.
       
        - `from django.urls import path, include`
    5. `path('articles/',include('articles.urls')),`넣는다.
       
       - 만약 `articles/*`라는 형식, articles라는 url까지만 보면 저쪽으로 넘긴다는 의미이다.
    6. 수정 이후
        ``` python
            from django.contrib import admin
        from django.urls import path, include
            from articles import views
    
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('articles/',include('articles.urls')),
        ]
        ```
    
16. 각 앱 디렉토리에 각 URL에 이름을 붙힐 수도 있다
    1. html 내의 출력값으로 `{% url 'artii_result' %}`
    2. `path('index/', views.index, name="index"),` 같은 방식으로 name으로 별칭을 명시해 준다.
    3. `app_name = 'articles'`같은 방식으로 태그도 붙혀준다.
       1. 태그를 붙혔을 때 위의 모습은 `{% url 'articles:artii_result' %}`
    4. 완성본
    ```python
    from django.urls import path
    from . import views

    app_name = 'articles'
    urlpatterns = [ 
        path('index/', views.index, name="index"),
        ...
    ]
    ```

## 장고의 리소스 관리
1. 장고는 기본적으로 templates를 app_name/templates에서 찾는다.
2. 장고는 기본적으로 static을 app_name/static에서 찾는다.

### 템플릿 상속
1. 앱의 베이스 디렉토리에 `templates`를 생성한다.
   
   - 이 경우에는 `firstapp/firstapp`디렉토리
2. 그리고 html 파일을 생성
3. ```django
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
       <!-- CSS only -->
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
   </head>
   <body>
       <div class="container">
           {# 이 블락 안에 자식 템플릿이 들어온다.#}
           {% block content %}
           {% endblock  %}
       </div>
   
   <!-- JS, Popper.js, and jQuery -->
   <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
   <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
   <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
   </body>
   </html>
   ```
4. {% block content %} {% endblock  %} 로 태그를 알려준다.
5. 그리고 원하는 html로 가서 {% extends 'base.html' %}로 상속을 선언한다.
6. {% block content %} {% endblock  %}로 템플릿에 포함 시킬 부분을 명시한다.
7. 마지막으로 setting.py
``` python
TEMPLATES = [
    {
        # 앱 디렉토리가 아니라 추가적으로 추가할 경로
        'DIRS': [
            # 점점 깊어지는 경로를 알려준다.
            # OS별로 /가 다르기 때문에 join으로 합쳐줘야한다.
            # 그래서 os.path로 os가 가지고 있는 /의 종류를 가져온다.
            os.path.join(BASE_DIR, 'firstapp', 'templates')
        ],
        ...
        'OPTIONS': {
            ...
        },
    },
]
```

### static
- 웹 사이트의 구성 요소 중에서 images, css, js파일과 같이 해당 내용이 고정되어, 응답을 할때도 별도의 처리 없이 파일 내용을 전부 가져온다.

1. 일단 static을 load한다
2. extends 밑에 `{% load static %}`
   
   - extends는 무조건 최상단이여야한다.
3. setting.py에 가서 static 밑에 붙힌다.
    ```python
    # 이걸 붙혀줘야 한다. 이 위치에 이미지를 저장함으로써 배포 시에도 이미지를 접근할 수 있게 한다.
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'firstapp', 'static'),
    ]
    ```
4. 그리고 firstapp의 하단에 static을 만들어 주고 pages의 static을 갖다 붙힌다.


1. URL로직 분리
   - 기본 URL이 바뀌어 버려 지금까지 작성된 모든 URL을 ㄱ다시 손봐줘야함.
   
   - 그건 어려우니 그냥 URL에 일믈 만들자
2. URL NAME
   - 그런데 두개의 앱의 URL이 같다면
   
   - 어떤 앱의 URL이름인지 app_name을 설정하자
3. URL NAMESPACE
   - 분명히 두번째 app의 index 주소로 요청을 보냈는데, 템플렛을 계속 첫번째 URL만 가져온다.
     - 한번에 합쳐서 관리 하기 때문에 첫번째 만 가져오는 것이다.
4. DjangoNameSpace
   - app_name/templates 이후에 app_name폴더를 하나 더 둠으로써 이름 공강을 생성한다.

    - 여러 페이지에 동일한 구조를 적용 시키고 싶다.
    - 템플렛의 자사용성에 초점
5. Template Inheritance