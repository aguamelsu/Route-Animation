import googlemaps
import folium
from PIL import Image
import io
import polyline
import imageio
from tqdm import tqdm
import random


API_KEY = #replace with your API key

gmaps = googlemaps.Client(key=API_KEY)


def route_coordinates(start, end):
    directions_result = gmaps.directions(start, end, mode="walking")

    coordinates = []

    for route in directions_result:
        for leg in route["legs"]:
            for step in leg["steps"]:
                l = polyline.decode(step['polyline']['points']) # Decoding coordinates from the polyline
                for pair in l:
                    coordinates.append({
                        "lat": pair[0],
                        "lng": pair[1]
                    })

    return coordinates
    

def map_mark(lat, lng):
    map = folium.Map(location=[lat, lng], zoom_start=16)

    rand_int = round(random.uniform(1, 9), 1)

    # Adding the markers based on CO2 levels
    folium.Marker(location=[lat, lng],
                icon = folium.Icon(color='green', icon='cloud') if rand_int <= 5 else folium.Icon(color='red', icon='cloud')
                ).add_to(map)
    return map


def animate(start, end):
    route = route_coordinates(start, end)

    images = []
    with tqdm(total=len(route), desc="Animating:", unit="frame") as pbar:
        for step in route:
            lat, lng = step['lat'], step['lng']
            map = map_mark(lat, lng)
            img_data = map._to_png(5)
            img = Image.open(io.BytesIO(img_data))
            images.append(img)
            pbar.update(1)  # Update progress bar

    # Save image as GIF
    imageio.mimsave('route1.gif', images, duration=1, loop=True)


if __name__ == "__main__":
    start = "St. Tropez, Supermanzana 18, 77505 Cancún, Q.R."
    end = "Av. Cumbres SM311 Lt47-01, 77533 Cancún, Q.R."

    animate(start, end)