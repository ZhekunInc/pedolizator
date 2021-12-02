from django.urls import path
from django.views.generic import TemplateView
from .views import HomePageView, HistoryList

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path(
        'rules/',
        TemplateView.as_view(
            template_name='main/rules.html',
            get_context_data=lambda: {'is_rules_page': True}
        ),
        name='rules'
    ),
    path(
        'history/', HistoryList.as_view(), name="history"
    )
]
