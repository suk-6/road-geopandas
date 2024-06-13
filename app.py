import os
import json
import fiona
import geopandas as gpd
from dotenv import load_dotenv

load_dotenv()

c = fiona.open(os.getenv("ROAD_PATH"), encoding="cp949")

shp = gpd.GeoDataFrame.from_features(c, crs="EPSG:5179").to_crs("epsg:4326")


def extract_boundary_coordinates(polygon_data, video_name):
    coordinates_list = []
    for polygon in polygon_data["geometry"]:
        exterior_coords = polygon.exterior.coords

        for coord in exterior_coords:
            coordinates_list.append(
                {
                    "lat": coord[1],
                    "lng": coord[0],
                    "video": video_name,
                }
            )

    return coordinates_list


seongdong_gu_data = shp[shp["SIG_KOR_NM"] == "성동구"]
coordinates_list = extract_boundary_coordinates(
    seongdong_gu_data, "Seongdong-gu boundary"
)

with open("seongdong_boundary.json", "w") as f:
    f.write(
        json.dumps({"name": "Seongdong-gu boundary", "coordinates": coordinates_list})
    )
