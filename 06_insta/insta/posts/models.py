from django.db import models
# 외부키의 데이터를 가져오기 위해서 호출한다.
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=200)
    image = models.ImageField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
