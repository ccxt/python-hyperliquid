import asyncio
import os
from random import randint
import sys
from pprint import pprint

root = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(root + '/hyperliquid')


import hyperliquid


def main():
    instance = hyperliquid.hyperliquid({})
    markets = instance.load_markets()
    ohlcv = instance.fetch_ohlcv("BTC/USDC:USDC", "1m")
    print(ohlcv)

asyncio.run(main())


