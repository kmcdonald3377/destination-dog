from django.conf.urls import url
from destination_dog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'articles', views.article_list, name='article'),
    url(r'dogoftheweek', views.dogofweek, name='dogoftheweek'),   
    url(r'locateservice', views.locateServices, name='locateservice'),
    url(r'events', views.events, name='events'),
    url(r'forum', views.forum, name='forum'),
    url(r'about', views.about, name='about'),
    url(r'contactus', views.contactus, name='contactus'),
    url(r'sitemap', views.sitemap, name='sitemap'),
]