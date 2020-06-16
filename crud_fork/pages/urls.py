from django.urls import path
from . import views

app_name="pages"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:index>/', views.detail, name="detail"),
    path('<int:index>/delete', views.delete, name="delete"),
    path('<int:index>/edit', views.edit, name="edit"),
    path('<int:index>/update', views.update, name="update"),
]