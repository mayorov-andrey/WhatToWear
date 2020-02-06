from django.views.generic.base import View


class PageNumberView(View):

    def get(self, request, *args, **kwargs):
        try:
            self.sort = self.request.GET["sort"]
        except KeyError:
            self.sort = "0"
        try:
            self.order = self.request.GET["order"]
        except KeyError:
            self.order = "A"
        try:
            self.search = self.request.GET["search"]
        except KeyError:
            self.search = ""
        try:
            self.tag = self.request.GET["tag"]
        except KeyError:
            self.tag = ""
        return super(PageNumberView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET["page"]
        except KeyError:
            pn = "1"
        self.success_url = self.success_url + "?page=" + pn
        try:
            self.success_url = self.success_url + "&search=" + request.GET["search"]
        except KeyError:
            pass
        try:
            self.success_url = self.success_url + "&tag=" + request.GET["tag"]
        except KeyError:
            pass
        return super(PageNumberView, self).post(request, *args, **kwargs)


