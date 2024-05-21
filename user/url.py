from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.page1),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^sendBack$',views.sendBack),
    url(r'^search$',views.search),  
    url(r'^emplogin$',views.emplogin),
    url(r'^emplanding$',views.emplanding),
]
