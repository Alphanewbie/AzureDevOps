"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# setting에 있는 static을 불러온다.
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
]
# 추가적인 설정인 느낌이기 때문에 따로 뺀다.
# 정적인 파일이기 때문에 static으로 접근을 하고, 사용자가 settings.MEDIA_URL의 주소를 요청을 하면
# document_root=settings.MEDIA_ROOT의 경로에 있는 파일을 보여준다.
# 사용자에게 실제 파일의 위치를 보여주지 않느낟.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
