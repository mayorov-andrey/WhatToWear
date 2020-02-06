from django.contrib.auth.decorators import login_required
from .views import CategoriesEdit
from django.urls import path

urlpatterns = [
    path('', login_required(CategoriesEdit.as_view()), name="categories_edit"),
]
