from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=100)
    due_date = models.DateField()
    # 장고의 장독 방식은 내 컴퓨터에 전역적으로settings.py라는 것이 선언되어 있는데
    # 이 프로젝트를 실행시키면 전역 적으로 선언되어 있는 것을 가져온 다음에 
    # 겹치는 부분을 지역적으로 선언되어 있는 setting를 덮어 씌워서 사용하는 것
    # settings에 상수로써 'auth.User'이라고 선언되어 있다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)