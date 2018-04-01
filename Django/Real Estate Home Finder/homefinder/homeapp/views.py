# from django.shortcuts import render
from django.views import generic
from .models import Location, Property


class IndexView(generic.ListView):
    template_name = 'homeapp/index.html'

    def get_queryset(self):
        return Location.objects.all()


class LocationView(generic.DetailView):
    model = Location
    template_name = 'homeapp/locationview.html'


class PropertyDetail(generic.DetailView):
    model = Property
    template_name = 'homeapp/propertyview.html'
