from django.urls import path,re_path
from .views import SlotCreateSet,SlotBookSet
urlpatterns = [
    path('host/', SlotCreateSet.as_view(),name="slot-create"),
    path('book/', SlotBookSet.as_view(),name="slot-update"),
   ]

   #r'^(?P<pk>\d+)/$'