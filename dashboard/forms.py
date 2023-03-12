from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_name', 'notes', 'car_model', 'start_booking_date', 'end_booking_date',)
        widgets = {
            'booking_name': forms.TextInput(),
            'car_model': forms.TextInput(),
            'notes': forms.Textarea(attrs={'rows': 5}),
            'start_booking_date': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_booking_date': forms.TextInput(attrs={'type': 'datetime-local'}),
        }