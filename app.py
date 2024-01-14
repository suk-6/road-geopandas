import os
import geopandas as gpd
from dotenv import load_dotenv

load_dotenv()

road = gpd.read_file(os.getenv("ROAD_PATH"))

ax = road.convex_hull.plot(color="red")
ax.set_axis_off()
ax.set_title("Convex Hull of Road Network")
ax.figure.savefig("convex_hull.png")
