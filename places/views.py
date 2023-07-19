from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Place


def show_index_page(request):
    places = Place.objects.all()
    context = {
        "geo_json": {
            "type": "FeatureCollection",
            "features": [],
        }
    }

    for place in places:
        place_features = {
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
                "detailsUrl": "/static/places/roofs24.json"
            }
        }
        context["geo_json"]["features"].append(place_features)
    return render(request, 'index.html', context=context)


def place_view(place_id):
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
