from django.conf.urls import include, url
from django.contrib import admin
from imdavemorrisonapp import views

urlpatterns = [
    url(r'^this/is/not/an/admin/page/', include(admin.site.urls)),
    url(r'^$', views.home, name='home')
]
