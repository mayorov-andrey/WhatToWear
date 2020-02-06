from django.urls import path, include
from .views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name="main"),
]