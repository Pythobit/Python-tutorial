# the file will be in root folder

import aiohttp
import asyncio
import time


async def fetch_page(url):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'page took {time.time() - start}')
            return response.status


loop = asyncio.get_event_loop()

tasks = [fetch_page('http://google.com') for i in range(30)]    # 50 coroutines object
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'All took {time.time() - start}')

