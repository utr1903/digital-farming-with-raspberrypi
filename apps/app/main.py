import logging
import time
import multiprocessing

from sensors import service as sensor_svc, mock
from dbs import service as db_svc, prometheus
from server import server

logging.basicConfig(level=logging.INFO)

def process_sensor_values():
    sensor_service = sensor_svc.SensorService([
        mock.SensorMock("sensor1", "plant1"),
        # dht22.SensorDHT22("sensor1", "plant1"),
    ])

    db_service = db_svc.DBService([
        prometheus.DBPrometheus(),
    ])

    while True:
        sensor_values = sensor_service.read_sensor_values()
        db_service.write_values(sensor_values)
        time.sleep(2.0)

def start_server():
    srv = server.Server()
    srv.run()

def main():
    processes = []
    processes.append(multiprocessing.Process(target=process_sensor_values))
    processes.append(multiprocessing.Process(target=start_server))
    
    for p in processes:
        p.start()

    for p in processes:
        p.join()

if __name__ == '__main__':
    main()
