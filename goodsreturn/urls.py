"""goodsreturn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('user.url')),
    url('home/',views.page1, name="home"),
    url('orderstat/',views.page4,name="clanding"),
    url('about/',views.about, name="about"),
    url('contact/',views.contact, name="contact"),
    url('reason/',views.reason,name="reason"),
    url('chkmail/',views.sendmail,name="one"),
    url('rd/',views.returndetails,name="rd"),
    url('event/', views.event, name='event'),
    url('peyechi/',views.peyechi),
    url('found/',views.found),
    url('fetch/',views.fetch),
    url('confirmpage/',views.page6,name='confirmpage'),
    url('confirmpagec/',views.page6c,name='confirmpagec'),
    url('returnhistory/',views.page10,name='returnhistory'),
    url('cslogin/',views.cslogin,name='cslogin'),
    url('rt/',views.reqlist, name='requestlist'),
    url('upload',views.upload, name='upload'),
    url('uploadc/',views.uploadc, name='uploadc'),
    url('returnlist/',views.boss,name='returnlist'),
    url('admin/',admin.site.urls),
    url('fuss/',views.fuss),
    url('huss/',views.huss),
    url('tuss/',views.tuss),
    url('muss/',views.muss,name="muss"),
    url('sendBack/',views.sendBack,name='sendback'),
    url('extract1/',views.extract1,name="extract1"),
    url('extract2/',views.extract2,name="extract2"),
    url('extract3/',views.extract3,name="extract3"),    
    url('chkatt/',views.attach),
    url('accept',views.accept),
    url('decline/',views.decline,name="decline"),
    url('fun/',views.fun,name="fun"),
    url('lala/',views.lala,name="lala"),
    url('goodspeed/',views.goodspeed),
    url('godspeed',views.godspeed),
    url('bothmail/',views.bothmail,name="moment"),
    url('index/',views.index,name="index"),
    #url('signup/',views.signup, name="signup"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
