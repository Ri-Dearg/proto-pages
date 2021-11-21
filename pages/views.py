from django.views.generic import ListView

from .models import PageData


class PageDataListView(ListView):
    """Renders the home page with a PageData List."""
    model = PageData
