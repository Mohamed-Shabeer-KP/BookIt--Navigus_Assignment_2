from rest_framework import generics, mixins
from .serializers import SlotCreateSerializer,SlotBookSerializer
from .permissions import IsOwnerOrReadOnly
from BookIt.models import Slot


class SlotCreateSet(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = SlotCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Slot.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     return Slot.objects.get(pk=pk)

    def perform_create(self, serializer):
        serializer.save(user_id = self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SlotBookSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SlotBookSerializer

    def get_queryset(self):
        return Slot.objects.all()
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}