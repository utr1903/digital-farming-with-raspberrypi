import random

from sensors import base

class SensorMock(base.SensorBase):

    def __init__(self, sensor_name, plant_name):
        super().__init__(sensor_name, plant_name)

    def read_temperature(self):
        return random.randint(10, 30)

    def read_humidity(self):
        return random.randint(40, 70)
