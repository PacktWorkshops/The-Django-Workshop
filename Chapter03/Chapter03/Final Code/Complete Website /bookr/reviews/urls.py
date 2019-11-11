from django.urls import path
from django.conf.urls import url
from .views import index, detail

urlpatterns = [
    url(r'^$', view=index),
    # /bookr/Advanced Deep Learning with Keras/
    # url(r'^(?P<book_title>[-\w]+)/$',views.titleDisplay , name = 'titleDisplay')
    path('<str:book_title>/', view=detail),
]
