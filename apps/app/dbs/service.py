
class DBService():

    def __init__(self, dbs):
        self.dbs = dbs

    def write_values(self, sensor_values):
        for sensor_name, sensor_data in sensor_values.items():
            plant_name = sensor_data["plant"]
            temperature = sensor_data["temperature"]
            humidity = sensor_data["humidity"]

            for db in self.dbs:
                try:
                    db.write_temperature(temperature, sensor_name, plant_name)
                    db.write_humidity(humidity, sensor_name, plant_name)
                except Exception as error:
                    print(error)
