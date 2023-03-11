from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('booking_name', 'slug', 'car_model', 'created_on', 'approved')
    search_fields = ['booking_name', 'car_model']
    prepopulated_fields = {'slug': ('booking_name',)}
    list_filter = ('created_on', 'start_booking_date')
    summernote_fields = ('content')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)