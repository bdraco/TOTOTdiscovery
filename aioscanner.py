import asyncio
import logging
import pprint

from TOTOTdiscovery.aioscanner import AIOTOTOTScanner

logging.basicConfig(level=logging.DEBUG)


async def go():
    scanner = AIOTOTOTScanner()
    pprint.pprint(await scanner.async_scan())


asyncio.run(go())
