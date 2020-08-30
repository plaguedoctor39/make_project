import csv
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'importing stations from file to DB'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'rt', encoding='UTF-8') as csv_file:
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            next(table_reader)
            for line in table_reader:
                table.append(line)
            print(table)
