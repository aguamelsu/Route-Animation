import googlemaps
import folium
from polyline import decode
import random
import time

API_KEY = #replace with your API key

gmaps = googlemaps.Client(key=API_KEY)

def route_coordinates(start, end):
    directions_result = gmaps.directions(start, end, mode="walking")

    coordinates = []

    for route in directions_result:
        for leg in route["legs"]:
            for step in leg["steps"]:
                l = decode(step['polyline']['points'])  # Decoding coordinates from the polyline
                for pair in l:
                    coordinates.append({
                        "lat": pair[0],
                        "lng": pair[1]
                    })

    return coordinates

def generate_map_html(route, markers):
    initial_lat, initial_lng = route[0]['lat'], route[0]['lng']
    map = folium.Map(location=[initial_lat, initial_lng], zoom_start=16)

    for step in route:
        lat, lng = step['lat'], step['lng']
        rand_int = round(random.uniform(1, 9), 1)
        color = 'green' if rand_int <= 5 else 'red'
        folium.Marker(location=[lat, lng], icon=folium.Icon(color=color, icon='cloud')).add_to(map)

    for marker in markers:
        folium.Marker(location=[marker['lat'], marker['lng']], icon=folium.Icon(color='blue', icon='info-sign')).add_to(map)

    return map._repr_html_()

if __name__ == "__main__":
    start = "St. Tropez, Supermanzana 18, 77505 Cancún, Q.R."
    end = "Av. Cumbres SM311 Lt47-01, 77533 Cancún, Q.R."

    route = route_coordinates(start, end)
    markers = []

    while True:
        # Simulate adding new markers
        new_marker = {
            'lat': route[len(markers)]['lat'],
            'lng': route[len(markers)]['lng']
        }
        markers.append(new_marker)

        # Generate updated HTML
        html_content = generate_map_html(route, markers)

        # Write HTML content to map.html
        with open('map.html', 'w') as f:
            f.write(html_content)

        # Adjust sleep time based on your preference
        time.sleep(5)  # Adjust the interval as needed
