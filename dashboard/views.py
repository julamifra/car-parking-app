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
        print("GEEEET")

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