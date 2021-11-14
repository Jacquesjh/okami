
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from pydantic import BaseModel
from shapely.geometry import Polygon, Point
from shapely import speedups
import plotly.express as px

from src.domain.entities.sensor import Sensor
from src.domain.entities.source import Source


class Room:

    sensors   : List[Sensor]
    sources   : List[Source]
    grid      : List[List[float]]
    vertices  : List[Tuple[float, float]]
    resolution: float
    

    def __init__(self, resolution: float = 0.25):
        self.resolution = resolution


    def plot_grid(self) -> None:
        
        x = self.x + [vertix[0] for vertix in self.vertices]
        y = self.y + [vertix[1] for vertix in self.vertices]
        fig = px.scatter(x = x, y = y)
        fig.show()


    def create_grid(self) -> None:

        if speedups.enabled == False:
            speedups.enable()

        valid_points = []

        vertices = self.vertices
        points   = [Point(vertix[0], vertix[1]) for vertix in vertices]

        # determine maximum edges
        polygon = Polygon(points)
        latmin, lonmin, latmax, lonmax = polygon.bounds
        resolution = 0.25

        points = []
        for lat in np.arange(latmin, latmax, resolution):
            for lon in np.arange(lonmin, lonmax, resolution):
                points.append(Point((round(lat,4), round(lon,4))))

        # validate if each point falls inside shape
        valid_points.extend([i for i in points if polygon.contains(i)])
        new_polygon = Polygon(valid_points)

        x = [point.coords.xy[0][0] for point in valid_points]
        y = [point.coords.xy[1][0] for point in valid_points]

        self.polygon = Polygon(valid_points)
        self.x = x
        self.y = y

    def set_vertixes(self, vertices: List[Tuple[float, float]]) -> None:

        self.vertices = vertices


    def enter_vertices(self) -> None:

        print(" ------- Please enter the vertices of the room ------- ")
        print(" ------- Use the following notation: 'x, y' -------")
        
        vertices = []
        while True:
            try:
                vertix = input()
                vertix = (float(vertix[0]), float(vertix[3]))
                vertices.append(vertix)
            except:
                break
        
        self.vertices = vertices

    def set_sensors(self, sensors: List[Sensor]) -> None:

        self.sensors = [sensor1, sensor2, sensor3, sensor4]


    def enter_sensors(self) -> None:

        print(" ------- Please enter the position of the sensors ------- ")
        print(" ------- Use the following notation: 'x, y' -------")

        sensors = []
        while True:
            try:
                sensor = input()
                sensor = (float(sensor[0]), float(sensor[3]))
                sensors.append(sensor)
            except:
                break

        self.sensors = sensors

# if __name__ == "__main__":
#     room = Room()

#     vertix1 = (0, 0)
#     vertix2 = (5, 0)
#     vertix3 = (0, 5)
#     vertix4 = (5, 5)

#     vertices = [vertix1, vertix2, vertix3, vertix4]

#     room.set_vertixes(vertices = vertices)

#     sensor1 = Sensor(x = 2, y = 1, z = 1.5)
#     sensor2 = Sensor(x = 2, y = 1, z = 1.5)
#     sensor3 = Sensor(x = 3, y = 2, z = 1.5)
#     sensor4 = Sensor(x = 2, y = 3, z = 1.5)

#     sensors = [sensor1, sensor2, sensor3, sensor4]
#     room.set_sensors(sensors = sensors)

#     room.create_grid()
#     room.plot_grid()
