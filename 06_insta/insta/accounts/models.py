from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # 그 클래스 내에서 클래스를 얻어올 수 없기 때문에 User로 받아오는건 불가능하다.
    # 그래서 settings.AUTH_USER_MODEL라고 해야한다.
    # 자기가 팔로우 하는 사람을 follow라는 이름으로 필드가 생긴다
    # 나를 팔로우 하는 사람을 follower라는 이름으로 필드가 생긴다
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower')
