from django.forms.models import modelformset_factory
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from .models import Category
from generic.mixins import CategoryListMixin


CategoriesFormset = modelformset_factory(Category, can_delete=True, fields='__all__')


class CategoriesEdit(TemplateView, CategoryListMixin):
    template_name = "categories_edit.html"
    formset = None

    def get(self, request, *args, **kwargs):
        self.formset = CategoriesFormset()
        return super(CategoriesEdit, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoriesEdit, self).get_context_data(**kwargs)
        context["formset"] = self.formset
        return context

    def post(self, request, *args, **kwargs):
        self.formset = CategoriesFormset(request.POST)
        if self.formset.is_valid():
            self.formset.save()
            messages.add_message(request, messages.SUCCESS, "Список категорий успешно изменен")
            return redirect("categories_edit")
        else:
            return super(CategoriesEdit, self).get(request, *args, **kwargs)