from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date,time
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse


from BookIt.models import Slot
User = get_user_model()
class SlotAPITestCase(APITestCase):
    def setUp(self):
        obj_user = User(username='testuser',email='test@mail.com')
        obj_user.set_password('password')
        obj_user.save() 
        obj_slots = Slot.objects.create(name='name',user_id = obj_user,status='Available',date=date(2019, 4, 13),start_time=time(10, 00, 00),end_time=time(11, 00, 00),attendee='someone')
    
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_slot(self):
        slot_count = Slot.objects.count()
        self.assertEqual(slot_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse('api-slot:slot-create')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
