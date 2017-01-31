from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.Post_list,name='Post_list'),
]