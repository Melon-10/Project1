import asyncio
import aiohttp

async def case_b():
    print('start', get_time(), 'case_b')
    await asyncio.sleep(1)
    print('end', get_time(), 'case_b')