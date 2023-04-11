from django.urls import path, include
from . import views

from .views import PersonListView, PersonCreateView, PersonDeleteView, PersonUpdateView

urlpatterns = [
    path("", PersonListView.as_view(), name="PersonList"),
    path("create/", PersonCreateView.as_view(), name="PersonCreate"),
    path("<pk>/delete/", PersonDeleteView.as_view(), name="PersonDelete"),
    path("<pk>/update/", PersonUpdateView.as_view(), name="PersonUpdate"),
]
