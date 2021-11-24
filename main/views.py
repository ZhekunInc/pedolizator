from django.shortcuts import render
from django.views.generic import ListView
from .models import Season


class HistoryList(ListView):

    template_name = "main/history.html"
    context_object_name = "seasons"

    def get_queryset(self):
        return Season.objects.filter(is_archive=True).order_by("title")
