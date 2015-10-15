"""choimirai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from choimirai.views import hello, current_datetime, hours_ahead, display_meta
from books import views
from books.contact.views import contact, thanks


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # url(r'^$', my_homepage_view),
    url(r'^displaymeta/$', display_meta),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
    url(r'^contact/thanks/$', thanks),
    url(r'^current_time/$', 'books.contact.views.current_time'),
    url(r'^books_for_author/$', 'books.views.books_for_author'),
    url(r'^publishers/$', views.PublisherList.as_view()),
    url(r'^publisher_detail/(?P<pk>\d+)/$', views.PublisherDetail.as_view()),
    url(r'^books/([\w-]+)/$', views.PublisherBookList.as_view()),
    url(r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author-detail'),
]
