"""SuddleVue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import MyApp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(MyApp.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]


"""
2020年的影响
大部分人有很多工作要做的
1上班的规范不能丢 
2 加强沟通分享以及技术解决方案上加强
3每一个决定都要和组长以及发哥沟通
"""
"""
接下来工作安排：导一个项目  写一个接口  用一个号码 测试

写一个记录  完成一个啥样的功能 还有哪些是待完成的 


"""