from django.contrib.auth.decorators import login_required
from .views import get_list, upload_file, delete
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('', login_required(get_list), name="imagepool_index"),
    path('upload/', login_required(upload_file), name="imagepool_upload"),
    path('<int:pk>/delete/', login_required(delete), name="imagepool_delete"),
]