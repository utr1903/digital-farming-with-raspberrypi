import asyncio
import time

from sensors import service as sensor_svc, mock
from dbs import service as db_svc, prometheus
from server import server

async def process_sensor_values(sensor_service, db_service):
    while True:
        sensor_values = sensor_service.read_sensor_values()
        print(sensor_values)
        db_service.write_values(sensor_values)
        await asyncio.sleep(2.0)

async def start_server(db_prometheus):
    srv = server.Server(db_prometheus)
    srv.run()

async def main():
    print(f"Started at {time.strftime('%X')}")

    sensor_service = sensor_svc.SensorService([
        mock.SensorMock("sensor1", "plant1"),
        # dht22.SensorDHT22("sensor1", "plant1"),
    ])

    db_prometheus = prometheus.DBPrometheus()
    db_service = db_svc.DBService([
        db_prometheus,
    ])

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(process_sensor_values(sensor_service, db_service))
        task2 = tg.create_task(start_server(db_prometheus))

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())
