
import random
from typing import List, Tuple

import numpy as np

# def ajust_sensors(room: Room, coord: Tuple[float, float], value: float) -> None:
#     for sensor in room.sensors:        
#         distance = pow(pow(coord[0] - sensor.x, 2) + pow(coord[1] - sensor.y, 2), 1/2)
#         sensor.value = value*pow(np.e, -pow(distance, 2)/ 1.5)


def random_timeseries(initial_value: float, volatility: float, count: int) -> List[float]:
    time_series = [initial_value]
    
    for i in range(count):
        time_series.append(time_series[-1] + initial_value*random.gauss(0, 1)*volatility)
    
    return time_series


def standardize(timeseries: List[float]) -> List[float]:
    timeseries = [num + abs(min(timeseries)) for num in timeseries]
    timeseries = [num/max(timeseries) for num in timeseries]

    return timeseries


def artificial_source(time_steps: int) -> List[Tuple[float, float]]:
    xseries = random_timeseries(1.25, 0.5, time_steps)
    xseries = np.array([3.75*x for x in standardize(xseries)])

    yseries = random_timeseries(1.25, 0.5, time_steps)
    yseries = np.array([3.75*y for y in standardize(yseries)])

    values  = random_timeseries(1.25, 0.25, time_steps)
    values  = standardize(values)
    values  = np.array([2000*v for v in values])

    return np.array((xseries, yseries, values))