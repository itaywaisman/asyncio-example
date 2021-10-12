import asyncio
import aiohttp
import uvloop


async def call_python_and_sleep(i):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print(f"got response {i}")
            await asyncio.sleep(1)
            return i


async def call_google_n_times(n):
    result = await asyncio.gather(*[call_python_and_sleep(i) for i in range(n)])
    print(result)


async def main():
    await call_google_n_times(10)


uvloop.install()
asyncio.run(main())
