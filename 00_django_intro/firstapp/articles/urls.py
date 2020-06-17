from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('dinner/', views.dinner),
    path('picsum/', views.picsum),
    # 밑에 2개는 같다. str이 디폴트 값이다.
    path('hello/<str:name>/',views.hello),
    path('hello/<name>/',views.hello),
    path('hello/<str:name>/<int:age>/',views.iam),
    path('multi/<int:num1>/<int:num2>/',views.multi),
    path('dtl',views.dtl_practice),
    path('palindrome/<str:word>',views.palindrome),
    path('throw',views.throw),
    path('catch/',views.catch),
    path('lotto-throw/', views.lotto_throw),
    path('lotto-catch/', views.lotto_catch),
    path('artii/', views.artii, name='artii'),
    path('artii-result/', views.artii_result, name='artii_result'),
]
