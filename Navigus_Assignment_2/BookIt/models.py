from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

class slot(models.Model):
    class Meta:
        verbose_name = ("slot_data")
        verbose_name_plural = ("slot_datas")

    def __str__(self):
        return self.name

    name = models.CharField("slot_name", max_length=20, on_delete=models.CASCADE)
    host_username = models.CharField("slot_host_username", max_length=30)
    status_choice = models.TextChoices('status','Available Booked')
    status = models.CharField("slot_status",blank=False,choices=status_choice.choices,max_length=10)
    date = models.DateField("slot_date")
    start_time = models.TimeField("slot_time_start",auto_now=False, auto_now_add=False)
    end_time = models.TimeField("slot_time_end",auto_now=False, auto_now_add=False)
    created_at = models.TimeField("slot_created_at",auto_now_add=True)
