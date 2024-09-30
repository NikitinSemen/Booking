from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import User
from booking.models import Reservation


class ReservationModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.reservation = Reservation.objects.create(
            user=self.user,
            table=3,
            date='2024-09-30',
            time='19:00',
            guests=2
        )

    def test_reservation_string_representation(self):
        self.assertEqual(str(self.reservation), f'{self.user}, {self.reservation.table}')

    def test_reservation_date_and_time(self):
        self.assertEqual(self.reservation.date, '2024-09-30')
        self.assertEqual(self.reservation.time, '19:00')


class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.client.login(email='testuser@example.com', password='password123')


