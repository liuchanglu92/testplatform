"""testplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

#定义http路由，是web系统的入口点
from web import views

urlpatterns =static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ [
    #path('', admin.site.urls),
    url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home),  #添加home/配置路径
]
handler404=views.page_not_found