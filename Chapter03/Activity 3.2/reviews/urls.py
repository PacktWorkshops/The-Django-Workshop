
from django.urls import path
from django.conf.urls import url
from .views import index , list_book,list_cont
from reviews import views


urlpatterns = [
    url(r'^$', view=index),
    url(r'booklist/$', view=list_book),
    url(r'contributorlist/$', view=list_cont),
    #/bookr/Advanced Deep Learning with Keras/
    # url(r'^(?P<book_title>[-\w]+)/$',views.titleDisplay , name = 'titleDisplay')
    path ('booklist/<str:book_title>/',views.detail_book , name = 'detail_book'),
    path ('contributorlist/<str:contributor_name>/',views.detail_contributor , name = 'detail_contributor'),
]

