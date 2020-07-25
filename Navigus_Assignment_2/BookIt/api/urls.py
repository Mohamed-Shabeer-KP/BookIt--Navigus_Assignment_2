from django.urls import path,re_path
from .views import SlotCreateSet,SlotBookSet
urlpatterns = [
    path('post/', SlotCreateSet.as_view(),name="slot-create"),
    re_path(r'^(?P<pk>\d+)/$', SlotBookSet.as_view(),name="slot-view"),
   ]

   