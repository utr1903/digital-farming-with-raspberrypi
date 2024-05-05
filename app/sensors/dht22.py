# import asyncio
# import board
# import adafruit_dht

from sensors import base

class SensorDHT22(base.SensorBase):

    def __init__(self, sensor_name, plant_name):
        super().__init__(sensor_name, plant_name)
        self.test = "XXX"
        # self.sensor = adafruit_dht.DHT22(board.D18)

    def read_temperature(self):
        return 20.0

    def read_humidity(self):
        return 50.0

    # async def read_values(self):
    #     while True:
    #         try:
    #             # Print the values to the serial port
    #             temperature = dhtDevice.temperature
    #             humidity = dhtDevice.humidity
    #             print(
    #                 "Temp: {:.1f} C / Humidity: {}% ".format(
    #                     temperature, humidity
    #                 )
    #             )

    #         except RuntimeError as error:
    #             # Errors happen fairly often, DHT's are hard to read, just keep going
    #             print(error.args[0])
    #             await asyncio.sleep(2.0)
    #             continue
    #         except Exception as error:
    #             dhtDevice.exit()
    #             raise error

    #         await asyncio.sleep(2.0)