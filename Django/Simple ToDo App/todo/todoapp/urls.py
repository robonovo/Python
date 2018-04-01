from django.conf.urls import url
from . import views

app_name = 'todoapp'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^done(?P<pk>[0-9]+)/$', views.DoneView.as_view(), name='done'),
    url(r'^faq', views.FaqView.as_view(), name='faq'),
]
