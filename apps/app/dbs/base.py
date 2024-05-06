from abc import ABC, abstractmethod

class DBBase(ABC):

    def __init__(self):
        pass

    def get_db_name(self):
        return self.db_name

    @abstractmethod
    def write_temperature(self, temperature):
        pass

    @abstractmethod
    def write_humidity(self, humidity):
        pass
