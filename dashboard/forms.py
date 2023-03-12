from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_name', 'car_model', 'start_booking_date', 'end_booking_date',)
        widgets = {
            'booking_name': forms.TextInput(attrs={'rows': 3}),
            'car_model': forms.TextInput(attrs={'rows': 3}),
            'start_booking_date': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_booking_date': forms.TextInput(attrs={'type': 'datetime-local'}),
        }