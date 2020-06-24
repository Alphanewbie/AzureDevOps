# 미리 선언되어 있는 유저 크리에이션 폼을 상속시켜서 만든다.
# 어지간해서는 장고가 선언해 놓은 것은 바꿔선 안된다.
from django.contrib.auth.forms import UserCreationForm
# 통상적으로는 이렇게 쓰지만, 이렇게 쓸 수는 있지만
# from .models import User
# 선언시 get_user_model 사용 가능하고 settings.py에 선언한 AUTH_USER_MODEL = 'accounts.User'을 가져온다.
from django.contrib.auth import get_user_model

# 유저 크리에이션 폼을 상속한다.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            # 패스워드
            'password1',
            # 패스워드 확인
            'password2',
            # 폰 넘버
            'phone',
            )