import csv
from django.core.management.base import BaseCommand
from project_app.models import Station, Route


class Command(BaseCommand):
    help = 'importing stations from file to DB'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'rt', encoding='cp1251') as csv_file:
            table_reader = csv.reader(csv_file, delimiter=';')
            next(table_reader)
            for line in table_reader:
                # print(line)
                routes_obj = []
                routes = line[7].split('; ')

                # print(routes_obj)
                Station.objects.create(latitude=line[3], longitude=line[2], name=line[1])
                station = Station.objects.last()
                print(station.name)
                for route in routes:
                    if Route.objects.filter(name=route):
                        route_obj = Route.objects.get(name=route)
                        print(f'маршрут {route} уже есть')
                        routes_obj.append(route_obj)
                    else:
                        Route.objects.create(name=route)
                        route_obj = Route.objects.get(name=route)
                        print(f'создание маршрута {route}')
                        routes_obj.append(route_obj)
                    station.routes.add(route_obj)
                    print(station)
                    # print(route_obj.stations.last())
                routes_obj.clear()
                break


            # print(Station.routes.first())


