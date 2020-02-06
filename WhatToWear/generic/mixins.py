from django.views.generic.base import ContextMixin
from categories.models import Category

class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        context["categories"] = Category.objects.all()
        return context


class PageNumberMixin(CategoryListMixin):
    def get_context_data(self, **kwargs):
        context = super(PageNumberMixin, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = 1
        return context
