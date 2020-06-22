from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/detail/', views.detail, name="detail"),
    path('<int:pk>/comment/create', views.comment_create, name="comment_create"),
    path('<int:page_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name="comment_delete"),
]