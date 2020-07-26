from rest_framework import generics, mixins
from .serializers import SlotCreateSerializer,SlotBookSerializer,SlotListSerializer
from .permissions import IsAuthenticated
from BookIt.models import Slot
from rest_framework.permissions import IsAuthenticated


class SlotCreateSet(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = SlotCreateSerializer

    def get_queryset(self):
        id = self.request.user.id
        return Slot.objects.filter(user_id=id)

    def perform_create(self, serializer):
        serializer.save(user_id = self.request.user)
        serializer.save(host = self.request.user.username)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

class SlotListSet(generics.ListAPIView):
    serializer_class = SlotListSerializer

    def get_queryset(self):
        return Slot.objects.all()
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

class SlotBookSet(generics.RetrieveUpdateAPIView):
    serializer_class = SlotBookSerializer        

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Slot.objects.filter(id=id)
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}


class SlotRemoveSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SlotBookSerializer

    def get_queryset(self):
        id = self.request.user.id
        return Slot.objects.filter(user_id=id)
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

