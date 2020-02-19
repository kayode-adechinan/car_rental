from django_filters.views import FilterView
from django.views.generic import DetailView

from car import models, filters



class CarListView(FilterView):
    template_name = "car/list.html"
    context_object_name = 'cars'  # Default: object_list
    paginate_by = 5
    filterset_class= filters.CarFilter

   
class CarDetailView(DetailView):
    model = models.Car
    template_name = 'car/detail.html'
    context_object_name = 'car'