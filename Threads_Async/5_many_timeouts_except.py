import asyncio


async def setTimeout(callback, delay):
    if delay > 2:
        raise Exception("Delay must be less than 2 seconds")
    await asyncio.sleep(delay)
    # if delay > 2:
    #     raise Exception("Delay must be less than 2 seconds")
    callback()
    return delay


async def chainTimeouts(*coros):
    # gather_result = asyncio.gather(*coros)
    gather_result = asyncio.gather(*coros, return_exceptions=True)
    result = await gather_result
    return result


def myCallback():
    print("setTimeout called")


result = asyncio.run(
    chainTimeouts(
        setTimeout(myCallback, 1), setTimeout(myCallback, 2), setTimeout(myCallback, 3), setTimeout(myCallback, 0.5)
    )
)

print(result)
