import board
import adafruit_dht

from sensors import base

class SensorDHT22(base.SensorBase):

    def __init__(self, sensor_name, plant_name):
        super().__init__(sensor_name, plant_name)

        self.device = adafruit_dht.DHT22(board.D18)

    def read_temperature(self):
        try:
            temperature = self.device.temperature
            print("Temperature: {:.1f}C".format(temperature))

        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:
            self.device.exit()
            raise error
        return temperature

    def read_humidity(self):
        try:
            humidity = self.device.humidity
            print("Humidity: {:.1f}%".format(humidity))

        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:
            self.device.exit()
            raise error
        return temperature
