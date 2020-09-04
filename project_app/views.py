from django.shortcuts import render
from .models import *

def show_stations(request):
    template = 'stations.html'
    stations = Station.objects.all()
    first_dot = Station.objects.first()
    second_dot = Station.objects.last()
    center = {'x': (first_dot.latitude + first_dot.longitude) / 2,
              'y': (second_dot.latitude + second_dot.longitude) / 2}
    print(stations)
    routes = Route.objects.all()
    if request.method == 'GET':
        print(request)
    context = {'stations': list(stations),
               'center': center,
               'routes': routes
               }
    return render(request, template, context)
