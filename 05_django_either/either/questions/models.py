from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    answer_a = models.CharField(max_length=100)
    answer_b = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Answer(models.Model):
    pass
    # chioce = 