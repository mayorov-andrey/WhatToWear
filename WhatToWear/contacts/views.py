from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class ContactsView(TemplateView, CategoryListMixin):
    template_name = "contacts.html"
