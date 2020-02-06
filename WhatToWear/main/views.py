from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from news.models import New
from goods.models import Good


class MainPageView(TemplateView, CategoryListMixin):
    template_name = "mainpage.html"
    news = New.objects.all()[0:5]
    goods = Good.objects.filter(featured=True)

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["news"]  = self.news
        context["goods"] = self.goods
        return context