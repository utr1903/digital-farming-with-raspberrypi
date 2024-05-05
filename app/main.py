import asyncio
import time

from sensors import service, dht22

async def read_sensor_values(sensor_service):
    return sensor_service.read_sensor_values()

async def process_sensor_values(sensor_service):
    while True:
        sensor_values = await read_sensor_values(sensor_service)
        print(sensor_values)
        await asyncio.sleep(2.0)

async def main():
    print(f"Started at {time.strftime('%X')}")

    sensor_service = service.SensorService([
        dht22.SensorDHT22("sensor1", "plant1"),
    ])

    await process_sensor_values(sensor_service)

    # async with asyncio.TaskGroup() as tg:
    #     task1 = tg.create_task(sensor.read_values())

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())
