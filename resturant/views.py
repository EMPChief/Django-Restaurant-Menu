from django.shortcuts import render
from django.views import generic
from .models import Dish

class MenuList(generic.ListView):
    queryset = Dish.objects.order_by('-date_created')
    template_name = 'resturant/index.html'
    context_object_name = 'meals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = Dish.MEAL_TYPES
        return context
    
class MenuDetail(generic.DetailView):
    model = Dish
    template_name = 'resturant/menu_detail.html'
