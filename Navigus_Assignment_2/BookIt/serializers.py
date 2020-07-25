from rest_framework import serializers

from .models import slot

class SlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = slot
        fields = ('name', 'host_username')