from abc import ABC, abstractmethod

class ActorBase(ABC):

    def __init__(self, sensor_name, plant_name):
        self.sensor_name = sensor_name
        self.plant_name = plant_name

    def get_actor_name(self):
        return self.sensor_name

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
