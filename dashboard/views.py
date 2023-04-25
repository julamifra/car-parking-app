from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking, User
from .forms import BookingForm


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class BookingCreation(View):
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "booking_creation.html",
            {
                "created": False,
                "booking_form": BookingForm()
            },
        )

    def post(self, request, *args, **kwargs):

        queryset = User.objects.filter(username=request.user.username)
        user = get_object_or_404(queryset)

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username

            booking = booking_form.save(commit=False)
            booking.author = user

            booking.save()
        else:
            booking_form = BookingForm()

        return render(
            request,
            "booking_creation.html",
            {
                "created": True,
                "booking_form": BookingForm()
            },
        )


class BookingEdition(View):

    def get(self, request, booking_id, *args, **kwargs):

        booking = get_object_or_404(Booking, id=booking_id)

        return render(
            request,
            "booking_edition.html",
            {
                "created": False,
                "booking_form": BookingForm(data={
                    'booking_name': booking.booking_name,
                    'car_model': booking.car_model,
                    'notes': booking.notes,
                    'start_booking_date': booking.start_booking_date,
                    'end_booking_date': booking.end_booking_date})
            },
        )

    def post(self, request, *args, **kwargs):

        queryset = User.objects.filter(username=request.user.username)
        user = get_object_or_404(queryset)

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username

            booking = booking_form.save(commit=False)
            booking.author = user

            booking.save()
        else:
            booking_form = BookingForm()

        return render(
            request,
            "booking_edition.html",
            {
                "created": True,
                "booking_form": BookingForm(data=request.POST)
            },
        )