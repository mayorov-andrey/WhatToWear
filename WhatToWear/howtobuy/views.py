from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class HowToBuyView(TemplateView, CategoryListMixin):
    template_name = "howtobuy.html"