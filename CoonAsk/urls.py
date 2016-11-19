"""CoonAsk URL Configuration

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
from sys import modules
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from CNAskApp.views import *


urlpatterns = [
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': 'uploads/'}),
    url(r'^$', index, name='index'),

    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^signup/', signup, name='signup'),
    url(r'^search/', search, name='search'),
    url(r'^profile/(?P<name>.*)$', profile, name='profile'),
    url(r'^ask/', ask, name='ask'),
    url(r'^question/(?P<id>.*)$', question, name='question'),
]


for category in CNPostSorting.categories():
    r_str = "^" + category["url"] + "/"

    if category["arg"] is not None:
        r_str += "(?P<cat_arg>.*)$"

    new_url = url(r_str,
                  getattr(modules[__name__], category["python_name"]),
                  name=category["name"])

    urlpatterns.append(new_url)
