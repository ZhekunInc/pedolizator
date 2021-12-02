
from django.utils import timezone
from django.views.generic import ListView
from datetime import datetime
from .models import Season, Stage


class HomePageView(ListView):
    template_name = 'main/homepage.html'
    context_object_name = "stages"

    def get_queryset(self):
        print(datetime.now())
        qs = Stage.objects.filter(match__end_at__gte=timezone.now())
        print(qs)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['is_homepage'] = True
        return ctx


class HistoryList(ListView):

    template_name = "main/history.html"
    context_object_name = "seasons"

    def get_queryset(self):
        return Season.objects.filter(is_archive=True).order_by("title")
