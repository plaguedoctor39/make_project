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
                # for obj in list(Station.objects.all()):
                #     print(obj.routes.all())
                # break
                # print(line)
                routes_obj = []
                routes_list = line[7].split('; ')
                for route in routes_list:
                    if Route.objects.filter(name=route):
                        route_obj = Route.objects.get(name=route)
                        # print(route_obj)
                        print(f'маршрут {route} уже есть')
                        routes_obj.append(route_obj)
                    else:
                        Route.objects.create(name=route)
                        route_obj = Route.objects.get(name=route)
                        print(f'создание маршрута {route}')
                        routes_obj.append(route_obj)
                print(routes_obj)
                station = Station.objects.create(latitude=line[3], longitude=line[2], name=line[1])
                station.save()
                print(station.routes.set(routes_obj))
                station.save()
                print(station.routes.all())
                print(route_obj.stations.last())
                # if len(Station.objects.all()) == 10:
                #     break

                routes_obj.clear()



            # print(Station.routes.first())


