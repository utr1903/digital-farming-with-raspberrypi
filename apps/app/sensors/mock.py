from sensors import base

class SensorMock(base.SensorBase):

    def __init__(self, sensor_name, plant_name):
        super().__init__(sensor_name, plant_name)

    def read_temperature(self):
        return 20.0

    def read_humidity(self):
        return 50.0
