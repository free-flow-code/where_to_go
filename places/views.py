from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Place


def show_index_page(request):
    places = Place.objects.all()

    context = {
        "geo_json": {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        place.lon,
                        place.lat,
                    ]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": reverse('place_json', args=[place.pk])
                }
            } for place in places]
        }
    }

    return render(request, 'index.html', context=context)


def show_place_json(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_details = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon
        }
    }
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
