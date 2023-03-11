from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('booking_creation/', views.BookingCreation.as_view(), name='booking_creation')
]