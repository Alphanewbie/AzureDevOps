from django.db import models

# Create your models here.
class Board(models.Model) :
    title = models.CharField(max_length=30)
    contents = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
