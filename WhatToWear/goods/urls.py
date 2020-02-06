from django.contrib.auth.decorators import permission_required
from .views import GoodListView, GoodDetailView, GoodCreate, GoodUpdate, GoodDelete
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', GoodListView.as_view(), name="goods_index"),
    path('<int:pk>/', GoodListView.as_view(), name="goods_index"),
    path('<int:pk>/detail/', GoodDetailView.as_view(), name="goods_detail"),
    path('<int:pk>/add/', permission_required("goods.add_good")(GoodCreate.as_view()), name="goods_add"),
    path('<int:pk>/edit/', permission_required("goods.change_good")(GoodUpdate.as_view()), name="goods_edit"),
    path('<int:pk>/delete/', permission_required("goods.delete_good")(GoodDelete.as_view()), name="goods_delete"),
]