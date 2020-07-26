from django.urls import path,re_path
from .views import SlotCreateSet,SlotBookSet,SlotListSet,SlotRemoveSet
urlpatterns = [
    path('post/', SlotCreateSet.as_view(),name="slot-create"),
    path('list/', SlotListSet.as_view(),name="slot-select"),
    re_path(r'^book/(?P<pk>\d+)/$', SlotBookSet.as_view(),name="slot-update"),
    re_path(r'^remove/(?P<pk>\d+)/$', SlotRemoveSet.as_view(),name="slot-remove"),
   ]

   