from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
# Create your views here.


class PersonListView(ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PersonCreateView(CreateView):
    model = Person
    fields = ['name', 'companyname', 'ic', 'date']
    template_name = "core/person_create.html"
    success_url = reverse_lazy('PersonList')


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('PersonList')


class PersonUpdateView(UpdateView):
    model = Person
    fields = ['name', 'companyname', 'ic', 'date']
    template_name = "core/person_update.html"
    success_url = reverse_lazy('PersonList')
