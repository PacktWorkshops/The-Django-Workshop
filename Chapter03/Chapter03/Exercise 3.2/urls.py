from django.urls import path
from django.conf.urls import url
from . views import index, detail, titleDisplay


urlpatterns =[ url(r'^$', view=index),
    #/bookr/22/
    url(r'^(?P<book_id>[0-9]+)/$',view = detail) ,
    #/bookr/Advanced Deep Learning with Keras/
    # url(r'^(?P<book_title>[-\w]+)/$',views.titleDisplay , name = 'titleDisplay')
    path ('<str:book_title>/',view = titleDisplay)
]

