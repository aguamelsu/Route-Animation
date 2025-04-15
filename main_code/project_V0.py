import googlemaps
import folium
from PIL import Image
import io
import json


API_KEY = #replace with your API key

gmaps = googlemaps.Client(key=API_KEY)


def route_coordinates(start, end):
    directions_result = gmaps.directions(start, end, mode="walking")

    coordinates = []

    for route in directions_result:
        for leg in route["legs"]:
            for step in leg["steps"]:
                coordinates.append({
                    "lat": step['start_location']['lat'], 
                    "lng": step['start_location']['lng'] 
                })

    return coordinates
    

def map_mark(lat, lng):
    map = folium.Map(location=[lat, lng], zoom_start=16)
    folium.Marker(location=[lat, lng]).add_to(map)
    return map


def map_images(route):
    saved_images = []

    for step in route:
        lat, lng = step['lat'], step['lng']
        map = map_mark(lat, lng)
        img_data = map._to_png(5)

        saved_images.append(Image.open(io.BytesIO(img_data)))

    return saved_images


def animate(saved_images):
    saved_images[0].save(
        "route.gif", save_all=True, append_images=saved_images[1:], duration=1000, loop=1
    )
    ...


start, end = "St. Tropez, Supermanzana 18, 77505 Cancún, Q.R.", "Av. Cumbres SM311 Lt47-01, 77533 Cancún, Q.R."

directions_result = gmaps.directions(start, end, mode="walking")
print(json.dumps(directions_result, indent=4))

#print(len(route_coordinates(start, end)))

#images = map_images(route)
#animate(images)

'''
start, end = "St. Tropez, Supermanzana 18, 77505 Cancún, Q.R.", "Av. Cumbres SM311 Lt47-01, 77533 Cancún, Q.R."

#directions_result = gmaps.directions(start, end, mode="walking")
#print(json.dumps(directions_result, indent=4))
#print(len(route_coordinates(start, end)))

route = route_coordinates(start, end)
images = map_images(route)
animate(images)
'''