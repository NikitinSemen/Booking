from django.contrib import admin
from .models import Reservation

admin.site.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time')
    search_fields = ('user__first_name',)