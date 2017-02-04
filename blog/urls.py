from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.Post_list,name='Post_list'),
    url(r'^Post/(?P<pk>\d+)/$' ,views.Post_detail,name='Post_detail'),
    url(r'^Post/new/$',views.Post_new),
    url(r'^Post/(?P<pk>\d+)/edit/$',views.Post_edit,name='Post_edit'),
    url(r'^drafts/$',views.Post_draft_list, name='Post_draft_list'),
    url(r'^Post/(?P<pk>\d+)/publish/$' ,views.Post_publish, name='Post_publish'),
    url(r'^Post/(?P<pk>\d+)/remove/$', views.Post_remove, name='Post_remove'),
]