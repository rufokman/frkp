from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *


class ParametersCreateView(CreateView):
    form_class = AddPostForm
    template_name = "frkpapp/param.html"
    success_url = 'history/'


class HistoryView(ListView):
    model = Queries
    template_name = "frkpapp/history.html"


class ParametersUpdateView(UpdateView):
    model = Queries
    form_class = AddPostForm
    template_name = 'frkpapp/param_update.html'
    success_url = reverse_lazy('history')


class ParametersDeleteView(DeleteView):
    model = Queries
    template_name = 'frkpapp/param_delete.html'
    success_url = reverse_lazy('history')


class ParametersSendView(TemplateView):
    template_name = "frkpapp/param_send.html"

    def get_context_data(self, **kwargs):
        data = get_object_or_404(Queries, pk=self.kwargs['pk'])
        data.status = 1
        data.save(update_fields=['status'])
