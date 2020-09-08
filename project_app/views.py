from django.shortcuts import render
from .models import *

def show_stations(request):
    template = 'stations.html'
    routes = Route.objects.all().order_by('name')

    if 'route' in request.GET:
        route_name = request.GET['route']
        route = Route.objects.get(name=route_name)
        stations = Station.objects.filter(routes=route)

        coordinates_x = stations.last().latitude - stations.first().latitude
        coordinates_y = stations.last().longitude - stations.first().longitude

        center_x = coordinates_x
        center_y = coordinates_y

        center = {'x': center_x, 'y': center_y}
        print(len(list(stations)))
        return render(request, template, {
            'routes': routes,
            'stations': stations,
            'center': center,
            'route': route_name,
        })

    context = {
               'routes': routes
               }
    return render(request, template, context)
