from django.db import models

# Create your models here.
class Pages(models.Model) :
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.TimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)