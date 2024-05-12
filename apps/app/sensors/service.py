import logging

logger = logging.getLogger(__name__)

class SensorService():

    def __init__(self, sensors):
        self.sensors = sensors

    def read_sensor_values(self):
        sensor_values = {}
        for sensor in self.sensors:

            # Get sensor data
            sensor_name = sensor.get_sensor_name()
            plant_name = sensor.get_plant_name()
            temperature = sensor.read_temperature()
            humidity = sensor.read_humidity()

            # Put into map
            sensor_values[sensor_name] = {
                "plant": plant_name,
                "temperature": temperature,
                "humidity": humidity,
            }

        logger.debug(sensor_values)
        return sensor_values