from django.urls import path,re_path
from .views import SlotCreateSet,SlotBookSet,SlotListSet
urlpatterns = [
    path('post/', SlotCreateSet.as_view(),name="slot-create"),
    path('list/', SlotListSet.as_view(),name="slot-list"),
    re_path(r'^(?P<pk>\d+)/$', SlotBookSet.as_view(),name="slot-view"),
   ]

   