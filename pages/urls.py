from django.urls import path

from .views import PageDataListView

urlpatterns = [
    path('', PageDataListView.as_view(), name="pagedata-list"),
]
