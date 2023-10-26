import asyncio


async def setTimeout(callback, delay):
    await asyncio.sleep(delay)
    callback()


def myCallback():
    print("setTimeout called")


asyncio.run(setTimeout(myCallback, 2))
