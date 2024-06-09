import json

from django.core.management.base import BaseCommand
from apps.location.models import GeoLocationDistances


class Command(BaseCommand):
    help = 'Load location distances from json'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument("--delete", action="store_true", help="Delete data before adding", )
        parser.add_argument("--delete-only", action="store_true", help="Delete data before adding", )

    def handle(self, *args, **options):
        if options['delete_only']:
            GeoLocationDistances.objects.all().delete()
            return

        if options['delete']:
            GeoLocationDistances.objects.all().delete()

        with open("data/geo_locations_distances.json", encoding='utf-8') as input_stream:
            locations_distances = json.load(input_stream)

        for distances_meta in locations_distances:
            origin_zone_id = distances_meta['ORIGIN_ZONE_ID']
            origin_name_geo = distances_meta['ORIGIN_NAME']
            dst_zone_id = distances_meta['DEST_ZONE_ID']
            dst_name_geo = distances_meta['DEST_NAME']
            distance = distances_meta['DISTANCE']
            duration = distances_meta['DURATION']

            location_distance = GeoLocationDistances(
                origin_zone_id=origin_zone_id,
                origin_name_geo=origin_name_geo,
                dest_zone_id=dst_zone_id,
                dest_name_geo=dst_name_geo,
                distance=distance,
                duration=duration
            )
            location_distance.save()

        self.stdout.write(self.style.SUCCESS(f'Added {len(locations_distances)} locations'))