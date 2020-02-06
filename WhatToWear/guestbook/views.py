from django.shortcuts import redirect
from django.views.generic.dates import ArchiveIndexView
from django.contrib import messages
from .models import GuestBook
from .forms import GuestBookForm
from generic.mixins import CategoryListMixin


class GuestBookView(ArchiveIndexView, CategoryListMixin):
    model = GuestBook
    date_field = "posted"
    template_name = "guestbook.html"
    paginate_by = 10
    allow_empty = True
    form = None

    def get(self, request, *args, **kwargs):
        self.form = GuestBookForm
        return super(GuestBookView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GuestBookView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = GuestBookForm(request.POST)
        if self.form.is_valid():
            if self.form.cleaned_data["honeypot"] == "":
                self.form.save()
                messages.add_message(request, messages.SUCCESS, "Запись успешно добавлена в гостевую книгу")
            return redirect("guestbook")
        else:
            return super(GuestBookView, self).get(request, *args, **kwargs)
