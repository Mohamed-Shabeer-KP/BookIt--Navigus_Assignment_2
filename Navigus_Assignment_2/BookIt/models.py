from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

class Slot(models.Model):
    class Meta:
        verbose_name = ("slot_data")
        verbose_name_plural = ("slot_datas")

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20,help_text='event name')
    user = models.CharField(max_length=40,help_text='host user name')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,help_text='host username')
    status_choice = models.TextChoices('status','Available Booked')
    status = models.CharField(blank=False,choices=status_choice.choices,max_length=10,help_text='status of slot')
    date = models.DateField(help_text='date for slot')
    start_time = models.TimeField(auto_now=False, auto_now_add=False,help_text='slot start time')
    end_time = models.TimeField(help_text='slot end time')
    created_at = models.TimeField(auto_now_add=True,help_text='slot created time')
    attendee = models.CharField(max_length=30,blank=True,help_text='attendee username')
