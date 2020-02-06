from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class AboutView(TemplateView, CategoryListMixin):
    template_name = "about.html"