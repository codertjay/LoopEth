import asyncio
import datetime
import time

from decouple import config
from web3 import Web3

x = datetime.datetime.now()

loop = asyncio.get_event_loop()


async def send_eth(value, gasPrice):
    web3 = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}')))
    try:
        if web3.eth.get_balance(config('FROM_ACCOUNT')) > 286982993542500:
            balance = web3.eth.get_balance(config('FROM_ACCOUNT'))
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            web3.eth.sendRawTransaction(
                web3.eth.account.signTransaction({
                    'chainId': 1,
                    'nonce': web3.eth.getTransactionCount(config('FROM_ACCOUNT'), 'pending'),
                    'to': config('TO_ACCOUNT'),
                    'value': int(balance * value),
                    'gas': 21000,
                    'gasPrice': int(balance * gasPrice / 21000)
                },
                    config('PRIVATE_KEY')).rawTransaction)
    except:
        balance = web3.eth.get_balance(config('FROM_ACCOUNT'))
        web3.eth.sendRawTransaction(
            web3.eth.account.signTransaction({
                'chainId': 1,
                'nonce': web3.eth.getTransactionCount(config('FROM_ACCOUNT'), 'pending'),
                'to': config('TO_ACCOUNT'),
                'value': int(balance * value),
                'gas': 21000,
                'gasPrice': int(balance * gasPrice / 21000)
            },
                config('PRIVATE_KEY')).rawTransaction)
    print("hello", value)


async def send_eth2(value, gasPrice):
    web3 = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}')))
    balance = web3.eth.get_balance(config('FROM_ACCOUNT'))
    try:
        web3.eth.sendRawTransaction(
            web3.eth.account.signTransaction({
                'chainId': 1,
                'nonce': web3.eth.getTransactionCount(config('FROM_ACCOUNT'), 'pending'),
                'to': config('TO_ACCOUNT'),
                'value': int(balance * value),
                'gas': 21000,
                'gasPrice': int(balance * gasPrice / 21000)
            },
                config('PRIVATE_KEY')).rawTransaction)
    except:
        web3.eth.sendRawTransaction(
            web3.eth.account.signTransaction({
                'chainId': 1,
                'nonce': web3.eth.getTransactionCount(config('FROM_ACCOUNT'), 'pending'),
                'to': config('TO_ACCOUNT'),
                'value': int(balance * value),
                'gas': 21000,
                'gasPrice': int(balance * gasPrice / 21000)
            },
                config('PRIVATE_KEY')).rawTransaction)


async def main(loop):
    while True:
        print(
            "Start : %s" % time.ctime())
        loop.create_task(send_eth(value=0.09, gasPrice=0.99))
        loop.create_task(send_eth(value=0.1, gasPrice=0.8))
        loop.create_task(send_eth(value=0.2, gasPrice=0.7))
        loop.create_task(send_eth(value=0.3, gasPrice=0.6))
        loop.create_task(send_eth(value=0.4, gasPrice=0.5))
        loop.create_task(send_eth(value=0.5, gasPrice=0.4))
        loop.create_task(send_eth(value=0.6, gasPrice=0.3))
        loop.create_task(send_eth(value=0.7, gasPrice=0.2))
        loop.create_task(send_eth(value=0.8, gasPrice=0.1))
        loop.create_task(send_eth2(value=0.09, gasPrice=0.99))
        loop.create_task(send_eth2(value=0.1, gasPrice=0.8))
        loop.create_task(send_eth2(value=0.2, gasPrice=0.7))
        loop.create_task(send_eth2(value=0.3, gasPrice=0.6))
        loop.create_task(send_eth2(value=0.4, gasPrice=0.5))
        loop.create_task(send_eth2(value=0.5, gasPrice=0.4))
        loop.create_task(send_eth2(value=0.6, gasPrice=0.3))
        loop.create_task(send_eth2(value=0.7, gasPrice=0.2))
        loop.create_task(send_eth2(value=0.8, gasPrice=0.1))
        print(
            "End : %s" % time.ctime())
        time.sleep(0.5)


try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
except:
    loop.close()
