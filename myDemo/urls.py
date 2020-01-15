"""myDemo URL Configuration

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
from blog import views
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),#网站首页
    path('show-<int:sid>.html', views.show, name='show'),#内容页
    path('archives/', views.archives, name='archives'), # 归档页
    path('categories/', views.categories, name='categories'),  # 分类页
    path('category_info/<int:categoryId>', views.category_info, name='category_info'), #分类列表页
    path('tags/', views.tags, name='tags'),  # 标签页
    path('tag_info/<tagId>', views.tag_info, name='tag_info'),#标签详情页
    path('s/', views.search, name='search'),#搜索列表页
    path('about/', views.about, name='about'),#联系我们单页
    url(r'mdeditor/', include('mdeditor.urls')),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
