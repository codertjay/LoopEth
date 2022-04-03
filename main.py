import asyncio
from decouple import config
from web3 import Web3
import datetime
from web3.eth import AsyncEth

loop = asyncio.get_event_loop()
x = datetime.datetime.now()


async def send_eth(value, balance):
    web3 = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}')))
    while True:
        if web3.eth.get_balance(config('FROM_ACCOUNT')) > 0:
            balance = web3.eth.get_balance(config('FROM_ACCOUNT'))
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            web3.eth.sendRawTransaction(
                web3.eth.account.signTransaction({
                    'chainId': 1,
                    'nonce': web3.eth.getTransactionCount(config('FROM_ACCOUNT'), 'pending'),
                    'to': config('TO_ACCOUNT'),
                    'value': int(balance * 0.09),
                    'gas': 21000,
                    'gasPrice': int(balance * 0.99 / 21000)
                },
                    config('PRIVATE_KEY')).rawTransaction)


async def main(loop):
    while True:
        loop.create_task(send_eth(value=0.09, balance=0.99))
        loop.create_task(send_eth(value=0.1, balance=0.8))
        loop.create_task(send_eth(value=0.2, balance=0.7))
        loop.create_task(send_eth(value=0.3, balance=0.6))
        loop.create_task(send_eth(value=0.4, balance=0.5))
        loop.create_task(send_eth(value=0.5, balance=0.4))
        loop.create_task(send_eth(value=0.6, balance=0.3))
        loop.create_task(send_eth(value=0.7, balance=0.2))
        loop.create_task(send_eth(value=0.8, balance=0.1))


try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
except:
    loop.close()
