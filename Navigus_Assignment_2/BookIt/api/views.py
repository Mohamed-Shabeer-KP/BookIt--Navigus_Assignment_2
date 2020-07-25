from rest_framework import generics
from .serializers import SlotCreateSerializer,SlotBookSerializer
from BookIt.models import Slot

class SlotCreateSet(generics.ListCreateAPIView):
    #lookup_field = 'host_name'
    queryset = Slot.objects.all().order_by('user')
    serializer_class = SlotCreateSerializer



class SlotBookSet(generics.ListAPIView):
    lookup_field = 'host_name'
    queryset = Slot.objects.all().order_by('user')
    serializer_class = SlotBookSerializer