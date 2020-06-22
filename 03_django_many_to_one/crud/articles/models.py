from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 밑에 선언되면 밑의 클래스_셋을 자동으로 선언한다.
    # comment_set = 
    # a.comment_set.all() 명령어로 몇개나 되는 것과 연결되어 있는걸 확인할 수 있다.
    # 사실은 Article 안에 들어가 있으므로 자동적으로 삭제된다.
    
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 상속키 : 매개변수로는 2개 
    # 1. 상속할 엔티티의 이름을 그대로 준다. : 필수
    # 2. 원본 삭제가 되었을때 같이 삭제 된다는 것을 알려준다 on_delete=models.CASCADE : 필수
    # 3. 이거는 객체를 가지고 있는 개념이다. 출력하면 위 객체 다 나옴
    article = models.ForeignKey(Article,on_delete=models.CASCADE)