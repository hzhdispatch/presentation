"""presentation URL Configuration

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
from django.urls import include, path
#import blog.views #导入主项目文件夹下的blog文件夹
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),#如果网址匹配，他会使用blog文件夹下的urls.py文件
    #path('blog/', blog.views.blog_page),这样不会造成不同views之间冲突
    path('',views.home),
    # 在views中创建一个home的function主页，当访问某个url时回调用home中的function返回一个网页
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) #前面写网址后面写文件目录
