from abc import ABC, abstractmethod

class SensorBase(ABC):

    def __init__(self, sensor_name, plant_name):
        self.sensor_name = sensor_name
        self.plant_name = plant_name

    def get_sensor_name(self):
        return self.sensor_name

    def get_plant_name(self):
        return self.plant_name

    @abstractmethod
    def read_temperature(self):
        pass

    @abstractmethod
    def read_humidity(self):
        pass
