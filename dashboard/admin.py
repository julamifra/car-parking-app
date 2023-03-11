from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('booking_name',)}
    summernote_fields = ('content')