from rest_framework import serializers
from BookIt.models import slot
import datetime as dt

class SlotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = slot
        fields = ('name','date','start_time','end_time')
        read_only_fields=['end_time']
    
    def validate(self,value):
        stime = value.get('start_time')
        time = str(stime)[3:5] #+ str(stime)[6:]
        print(time)
        if not int(time) == 0:
            raise serializers.ValidationError("Starting time should be Fixed Hour (For example, 01:00:00, 12:00:00, 13:00:00, etc)")

        if value.get('end_time',None)==None:
            delta = dt.timedelta(hours=1)
            value['end_time'] = (dt.datetime.combine(dt.date(1,1,1),stime) + delta).time()
        return value

    def validate_name(self,value):
        obj = slot.objects.filter(name=value)
        if obj.exists():
            raise serializers.ValidationError("An event with the name you have entered is already present.please enter another name.")
        return value