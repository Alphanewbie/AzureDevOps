from django.db import models
# 외부키의 데이터를 가져오기 위해서 호출한다.
from django.conf import settings
from imagekit.models import ProcessedImageField
# 이미지를 잘라서 맞춘다.
from imagekit.processors import ResizeToFill
# 이건 이미지 크기를 줄이는 것
# from imagekit.processors import ResizeToFit

#M-N관계의 장점은 서로간의 데이터를 찾아올 수 있당!

# 예를 들면 
# class User:
#   post_set = FK => 어떤 유저가 작성한 글들
#   post_set = M2M => 어떤 유저가 좋아요 버튼 누른 글들
#   즉 User에서 post_set을 했을 때, 둘 중 무엇을 내보내야 하냐는 뜻이다.

# related_name='like_posts' 속성으로
# post_set = M2M => 어떤 유저가 좋아요 버튼
# 이
# like_posts = M2M =>어떤 유저가 좋아요 버튼
# 가 되었다.

# 각각
# User에서는 user.like_post
# post에서는 post.like_user로 각각 찾아올 수 있다.

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=200)
    # 작성한 사람을 저장
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField()
    image = ProcessedImageField(upload_to='media',
                                            # 500,500으로 바꾸고 양 사이드에 검은색을 채울 것인가.
                                           processors=[ResizeToFill(500, 500)],
                                           format='JPEG',
                                            # 퀄리티이다.
                                           options={'quality': 60})
    # 여러개를 넣을 수 있는 것. 이것만 넣으면 에러가 난다.
    # 왜냐하면 위에 유저랑 연결 1:n으로 연결되어 있는데 다시 n:m으로 연결한다고 하니까 에러
    # 좋아요 버튼을 누른 사람들을 저장
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # related_name=로 연결 네임을 정해준다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    
    # ID 순으로 역순으로 정렬하겠다는 뜻이다.
    class Meta:
        ordering = ['-id']