from django.shortcuts import render
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
