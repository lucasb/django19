from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<id>[0-9]+)/$', views.post_detail),
    url(r'^post/(?P<id>[0-9]+)/edit$', views.post_edit),
    url(r'^post/(?P<id>[0-9]+)/publish/$', views.post_publish),
    url(r'^post/(?P<id>[0-9]+)/delete/$', views.post_delete),
    url(r'^post/new/$', views.post_new),
    url(r'^post/drafts/$', views.post_draft_list),
]
