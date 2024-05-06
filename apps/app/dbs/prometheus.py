from prometheus_client import Gauge, generate_latest

from dbs import base

class DBPrometheus(base.DBBase):

    def __init__(self):
        super().__init__()
        self.db_name = "prometheus"
        self.metrics = {
            "temperature": Gauge(
                name="digital_farming_temperature",
                documentation="Temperature read from the sensor",
                labelnames=["sensor", "plant"],
                unit="celcius",
            ),
            "humidity": Gauge(
                name="digital_farming_humidity",
                documentation="Humidity read from the sensor",
                labelnames=["sensor", "plant"],
                unit="percentage",
            ),
        }

    def write_temperature(self, temperature, sensor_name, plant_name):
        print(temperature)
        self.metrics["temperature"].labels(
            sensor=sensor_name,
            plant=plant_name,
        ).set(temperature)

    def write_humidity(self, humidity, sensor_name, plant_name):
        self.metrics["humidity"].labels(
            sensor=sensor_name,
            plant=plant_name,
        ).set(humidity)
