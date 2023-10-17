from web3.auto import Web3
import asyncio
import json

# enter your web socket node credentials here
# this will allow us to stream transactions
wss = 'wss://bold-sly-resonance.quiknode.pro/aa862642de3dcdad72ab18e5ac7c6babfaec8461/'
web3 = Web3(Web3.WebsocketProvider(wss))