from django.views.generic import ListView, DetailView
from .models import Task


class IndexView(ListView):
    template_name = 'todoapp/index.html'

    def get_queryset(self):
        return Task.objects.all()


class DetailView(DetailView):
    model = Task
    template_name = 'todoapp/detail.html'


class DoneView(DetailView):
    model = Task
    template_name = 'todoapp/done.html'


class FaqView(ListView):
    model = Task
    template_name = 'todoapp/faq.html'
