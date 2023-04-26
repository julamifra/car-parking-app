from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking, User
from .forms import BookingForm
from django.contrib import messages


class BookingList(generic.ListView):
    model = Booking
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        try:
            if self.request.user.is_authenticated:
                user = self.request.user
                return Booking.objects.filter(author=user).order_by('-created_on')
            else:
                return Booking.objects.order_by('-created_on')
        except Exception as e:
            print('%s' % e)


class BookingCreation(View):
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "booking_creation.html",
            {
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

            messages.success(request, 'Your booking has been sent and is awaiting approval')  
            return redirect('home')

        return render(
            request,
            "booking_creation.html",
            {
                "booking_form": booking_form
            },
        )


class BookingEdition(View):

    def get(self, request, booking_id, *args, **kwargs):

        booking = get_object_or_404(Booking, id=booking_id)

        return render(
            request,
            "booking_edition.html",
            {
                "booking_form": BookingForm(data={
                    'booking_name': booking.booking_name,
                    'car_model': booking.car_model,
                    'notes': booking.notes,
                    'start_booking_date': booking.start_booking_date,
                    'end_booking_date': booking.end_booking_date}),
                "booking_id": booking.id
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

        messages.success(request, 'Your booking has been saved correctly and is awaiting approval')

        return render(
            request,
            "booking_edition.html",
            {
                "booking_form": BookingForm(data=request.POST),
                "booking_id": booking.id
            },
        )


def delete_booking(request, booking_id):
    data = get_object_or_404(Booking, id=booking_id)
    data.delete()
    messages.success(request, f'Successfully removed booking: {data.booking_name}')
    return redirect('home')