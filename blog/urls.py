from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<id>[0-9]+)/$', views.post_detail),
]
