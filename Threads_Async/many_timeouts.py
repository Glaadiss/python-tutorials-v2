import asyncio


async def setTimeout(callback, delay):
    await asyncio.sleep(delay)
    callback()


async def chainTimeouts(*coros):
    gather_result = asyncio.gather(*coros)
    result = await gather_result
    print(result)


def myCallback():
    print("setTimeout called")


asyncio.run(chainTimeouts(setTimeout(myCallback, 1), setTimeout(myCallback, 2)))
