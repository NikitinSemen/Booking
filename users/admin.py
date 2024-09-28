from django.contrib import admin
from .models import User

@admin.register(User)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'avatar')
    search_fields = ('user__email',)

