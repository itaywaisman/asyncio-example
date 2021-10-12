import asyncio
from concurrent.futures import ThreadPoolExecutor

import uvloop
import pandas as pd


def long_sync_code():
    df = pd.read_csv('MOCK_DATA.csv')
    return df.describe()


async def sync_code_wrapper():
    loop = asyncio.get_event_loop()

    # with ProcessPoolExecutor() as executor:
    # with CeleryExecutor() as executor: - doesn't exists currently
    # with RayExecutor() as executor: - doesn't exists currently
    with ThreadPoolExecutor() as executor:
        return await loop.run_in_executor(executor, long_sync_code)


async def run_sync_code_n_times(n):
    results = await asyncio.gather(*[sync_code_wrapper() for i in range(n)])
    print(results)


async def main():
    await run_sync_code_n_times(3)


uvloop.install()
asyncio.run(main())

