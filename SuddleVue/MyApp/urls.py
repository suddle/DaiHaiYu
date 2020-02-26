from django.conf.urls import url, include

from MyApp.views.views import add_book,show_books

urlpatterns = [
    # url(r'^add_book/', include(MyApp.urls.urlpatterns)),
    url(r'add_book/', add_book, name='add_book'),
    url(r'show_books/', show_books, name='show_books'),
]