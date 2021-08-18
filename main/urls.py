from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name='main/homepage.html',
            get_context_data=lambda: {'is_homepage': True}
        ),
        name='home_page'
    ),
]