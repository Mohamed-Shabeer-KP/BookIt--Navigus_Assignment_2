from rest_framework import generics
from .serializers import SlotCreateSerializer
from BookIt.models import slot

class SlotCreateSet(generics.ListCreateAPIView):
    #lookup_field = 'pk'
    queryset = slot.objects.all().order_by('username')
    serializer_class = SlotCreateSerializer