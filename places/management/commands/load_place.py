import os
import json
import requests
from urllib.parse import urlsplit
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


def get_image(image_link):
    response = requests.get(image_link)
    response.raise_for_status()
    return ContentFile(response.content)


class Command(BaseCommand):
    help = 'Upload places to DB from JSON'

    def add_arguments(self, parser):
        parser.add_argument('json_folder', type=str, help='Path to folder with json files.')

    def handle(self, *args, **options):
        folder = options['json_folder']
        json_files = [
            os.path.join(folder, filename) for filename in os.listdir(folder)
            if filename.endswith('.json')
        ]
        place_jsons = []

        for file in json_files:
            with open(file, 'r', encoding='utf8') as json_file:
                place_jsons.append(json.load(json_file))

        for place in place_jsons:
            place_object, _ = Place.objects.get_or_create(
                title=place['title'],
                defaults={
                    'description_short': place['description_short'],
                    'description_long': place['description_long'],
                    'lat': place['coordinates']['lat'],
                    'lon': place['coordinates']['lng']
                }
            )

            for image_link in place['imgs']:
                content = get_image(image_link)
                image_name = str(urlsplit(image_link).path.split('/')[-1])
                image_object = Image.objects.create(place=place_object)
                image_object.image.save(image_name, content=content, save=True)

        self.stdout.write(self.style.SUCCESS('Successfully add all places.'))
