import datetime

from decouple import config
from web3 import Web3

x = datetime.datetime.now()

web3 = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}')))

print(web3.eth.get_balance(config('FROM_ACCOUNT')))
