from django.conf.urls import url, include

from MyApp.views.login import logins, regist, logouts
from MyApp.views.Pics import getpic

from MyApp.views.views import add_book,show_books

urlpatterns = [
    # url(r'^add_book/', include(MyApp.urls.urlpatterns)),
    url(r'add_book/', add_book, name='add_book'),
    url(r'show_books/', show_books, name='show_books'),
    url(r'login/', logins, name='login'),
    url(r'regist/', regist, name='regist'),
    url(r'logout/', logouts, name='logout'),
    url(r'getpic/', getpic, name='getpic'),
]