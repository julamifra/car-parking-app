from .models import Booking
from django import forms
from datetime import datetime
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_name', 'notes', 'car_model', 'start_booking_date', 'end_booking_date',)
        widgets = {
            'booking_name': forms.TextInput(attrs={
                'maxlength': '100'
            }),
            'car_model': forms.TextInput(attrs={
                'maxlength': '100'
            }),
            'notes': forms.Textarea(attrs={'rows': 5, 'maxlength': '1000'}),
            'start_booking_date': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_booking_date': forms.TextInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        super(BookingForm, self).clean()

        start_booking_date = self.cleaned_data.get('start_booking_date')
        end_booking_date = self.cleaned_data.get('end_booking_date')

        if start_booking_date.timestamp() < timezone.now().timestamp():
            self._errors['start_booking_date'] = self.error_class(['The start date should be after today'])
        
        return self.cleaned_data