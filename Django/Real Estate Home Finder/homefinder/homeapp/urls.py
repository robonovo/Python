from django.conf.urls import url
from . import views

urlpatterns = [
    # /homeapp/      Home Page
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /homeapp/x     Locations Page
    url(r'^(?P<pk>[0-9]+)/$', views.LocationView.as_view(), name='location'),
    # /homeapp/x/y   Property Details Page
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/$', views.PropertyDetail.as_view(), name='property'),
]
