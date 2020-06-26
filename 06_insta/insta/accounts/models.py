from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.


class User(AbstractUser):
    # 그 클래스 내에서 클래스를 얻어올 수 없기 때문에 User로 받아오는건 불가능하다.
    # 그래서 settings.AUTH_USER_MODEL라고 해야한다.
    # 자기가 팔로우 하는 사람을 follow라는 이름으로 필드가 생긴다
    # 나를 팔로우 하는 사람을 follower라는 이름으로 필드가 생긴다
    follow = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='follower')
    # upload_to='accounts'그 media폴더 안에 하위 디렉토리를 만들고 넣는다.
    image = ProcessedImageField(
                        upload_to='accounts',   
                        # 500,500으로 바꾸고 양 사이드에 검은색을 채울 것인가.
                        processors=[ResizeToFit(300, 300)],
                        format='JPEG',
                        # 퀄리티이다.
                        options={'quality': 60},
                        default="default.jpg"
                        )
