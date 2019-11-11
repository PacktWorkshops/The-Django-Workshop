
from django.conf.urls import url
from .views import index , list_book,list_cont



urlpatterns = [
    url(r'^$', view=index),
    url(r'booklist/$', view=list_book),
    url(r'contributorlist/$', view=list_cont)
]

