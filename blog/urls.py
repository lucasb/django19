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
    url(r'^post/(?P<id>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<id>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<id>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^thrends/$', views.thrends_tags)
]
