장고는 기본적으로 로그인 테이블을 제공한다.
참고 : https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/

1. 로그인 폼을 보여주는 것로 로그인 기능을 가져온다. `from django.contrib.auth.forms import UserChangeForm`

2.  ``` python
    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid() :
                form.save()
                return redirect('account:login')
            pass
        else:
            form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'account/signup.html', context)
    ```

3. 장고 패스워드 의미
```
algorithm: pbkdf2_sha256 iterations: 180000 salt: DlWbT5****** hash: 3HHfVT**************************************
Raw passwords are not stored, so there is no way to see this user’s password, but you can change the password using this form.
```
패스워드를 받아서 소금을 치고 sha256 해싱으로 단방향 해싱을 한다.

4. 로그인은 `AuthenticationForm(forms.Form):`을 쓰는데 `(forms.Form)`이기 때문에 모양이 달라진다.
    ```python
    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                # 폼 안의 유저 데이터를 가지고 온다.
                auth_login(request, form.get_user())
                return redirect('todo:index')
        else:
            form = AuthenticationForm()
        context = {
            'form' : form,
        }
        return render(request,'account/login.html', context)
    ```

5. 로그인 해서 들어가면 관리자 도구의 application 탭의 쿠키 앱에 세션과 쿠기가 들어가 있는 것을 확인할 수 있다.
6. `{{ user }}`는 선언 안해도 자동으로 쓸 수 있다.
    -  `{{ user }}`과
    -  `{{ user.username }}`은 다르다. 위는 로그인 안 했으면 Annomnouse 유저를 쓴다. 보통 이것을 쓰자

7. 
``` django
    {% if user.is_authenticated  %}
        <a href="{% url 'todo:index' %}">인덱스</a>
        <span> {{ user.username }}님 환영합니다. </span>
    {% else %}
        <a href="{% url 'account:signup' %}">회원가입</a>
        <a href="{% url 'account:login' %}">로그인</a>
    {% endif %}
```
8. `from django.contrib.auth import logout as auth_logout`
    - `auth_logout(request)` : 로그아웃 시키는 함수
