from prometheus_client import Gauge

from dbs import base

class DBPrometheus(base.DBBase):

    def __init__(self):
        super().__init__()
        self.db_name = "prometheus"
        self.temperature = Gauge(
            name="digital_farming_temperature",
            documentation="Temperature read from the sensor",
            labelnames=["sensor", "plant"],
            unit="celcius"
        )
        self.humidity = Gauge(
            name="digital_farming_humidity",
            documentation="Humidity read from the sensor",
            labelnames=["sensor", "plant"],
            unit="percentage"
        )

    def write_temperature(self, temperature):
        self.temperature.set(temperature)

    def write_humidity(self, humidity):
        self.humidity.set(humidity)