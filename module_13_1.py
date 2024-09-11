import asyncio
import time


async def start_strongman(name,power):
    print(f"Силач {name} начал соревнования.")
    t1 = 1/power
    for i in range(1, 6):
        await asyncio.sleep(t1)
        print(f"Силач {name} поднял {i} шар.")
    print(f"Силач {name} закончил соревнования")


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Пашка',4))
    task2 = asyncio.create_task(start_strongman('Лунтик',3))
    task3 = asyncio.create_task(start_strongman('Максим',5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
