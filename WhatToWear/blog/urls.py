from django.contrib.auth.decorators import permission_required
from .views import BlogListView, BlogDetailView, BlogCreate, BlogUpdate, BlogDelete
from django.urls import path

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),
    path('<int:pk>/detail/', BlogDetailView.as_view(), name="blog_detail"),
    path('add/', permission_required("blog.add_blog")(BlogCreate.as_view()), name="blog_add"),
    path('<int:pk>/edit/', permission_required("blog.change_blog")(BlogUpdate.as_view()), name="blog_edit"),
    path('<int:pk>/delete/', permission_required("blog.delete_blog")(BlogDelete.as_view()), name="blog_delete"),
]