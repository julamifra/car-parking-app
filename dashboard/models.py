from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# STATUS = ((0, "Draft"), (1, "Published"))
class Booking(models.Model):
    booking_name = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dashboard_bookings"
    )
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()
    # status = models.IntegerField(choices=STATUS, default=0)
    start_booking_date = models.DateTimeField()
    end_booking_date = models.DateTimeField()
    car_model = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.author.username
