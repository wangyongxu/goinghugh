"""goinghugh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout
from blogs.views import index,blog,new_blog_form,new_blog_post,index_login,index_register,article_to_blog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index,name='index'),
    url(r'^blog/(?P<page>\d+)/$', blog,name='blog'),
    url(r'^comment/(?P<id>\d+)/$', article_to_blog,name='comment'),
    url(r'^new_blog/$', new_blog_form,name='new_blog_form'),
    url(r'^post_blog/$', new_blog_post,name='new_blog_post'),
    url(r'^login/$', index_login,name='login'),
    url(r'^logout/$', logout,{'next_page':'/'},name='logout'),
    url(r'^register/$', index_register,name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)