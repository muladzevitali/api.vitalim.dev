import json

from django.core.management.base import BaseCommand

from apps.location.models import Location


class Command(BaseCommand):
    """Command for initializing data to user app: user"""
    help = 'Initialize locations data from json file'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument("--delete", action="store_true", help="Delete data before adding", )
        parser.add_argument("--delete-only", action="store_true", help="Delete data before adding", )

    def handle(self, *args, **options):
        if options['delete_only']:
            Location.objects.all().delete()
            return

        if options['delete']:
            Location.objects.all().delete()

        with open("data/cadastre.json", encoding='utf-8') as input_stream:
            locations_meta = json.load(input_stream)

        for location_meta in locations_meta:
            zone_id = location_meta["ZONE_ID"]
            sector_id = location_meta.get("SECTOR_ID")
            name_en = location_meta["NAME_EN"]
            name_geo = location_meta["NAME_GEO"]
            latitude = location_meta["LATITUDE"]
            longitude = location_meta["LONGITUDE"]
            country_en = location_meta.get('COUNTRY_EN') or 'geo'
            country_geo = location_meta.get('COUNTRY_GEO') or 'საქართველო'
            location_type = Location.TypeEnum.CITY if sector_id is None else Location.TypeEnum.VILLAGE

            location = Location(
                name_en=name_en,
                name_geo=name_geo,
                country_en=country_en,
                country_geo=country_geo,
                location_type=location_type,
                zone_id=zone_id,
                sector_id=sector_id,
                latitude=latitude,
                longitude=longitude
            )
            location.save()

        self.stdout.write(self.style.SUCCESS(f'Added {len(locations_meta)} locations'))
