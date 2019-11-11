
from django.conf.urls import  url
from .views import index , detail


urlpatterns = [
    url(r'^$', view=index),
    #/bookr/22/
    url(r'^(?P<book_id>[0-9]+)/$',view = detail)

]
