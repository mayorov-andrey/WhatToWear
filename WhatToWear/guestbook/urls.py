from django.urls import path
from .views import GuestBookView

urlpatterns = [
    path('', GuestBookView.as_view(), name="guestbook"),
]