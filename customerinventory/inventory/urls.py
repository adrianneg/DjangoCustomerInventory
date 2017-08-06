from django.conf.urls import url, include
from .views import (index,item_detail)
# from . import views as post_views
# using post_views.post_update

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^item/(?P<id>\d+)/', item_detail, name="item_detail"),
]
