import asyncio
import time

from sensors import service, mock
from server import server

async def read_sensor_values(sensor_service):
    return sensor_service.read_sensor_values()

async def process_sensor_values(sensor_service):
    while True:
        sensor_values = await read_sensor_values(sensor_service)
        print(sensor_values)
        await asyncio.sleep(2.0)

async def start_server():
    srv = server.Server()
    srv.run()

async def main():
    print(f"Started at {time.strftime('%X')}")

    sensor_service = service.SensorService([
        mock.SensorMock("sensor1", "plant1"),
        # dht22.SensorDHT22("sensor1", "plant1"),
    ])

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(process_sensor_values(sensor_service))
        task2 = tg.create_task(start_server())

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())
