from web3.auto import Web3
import asyncio
import json

wss = 'wss://bold-sly-resonance.quiknode.pro/aa862642de3dcdad72ab18e5ac7c6babfaec8461/'
web3 = Web3(Web3.WebsocketProvider(wss))

# Check to see if you are connected to your node
print(web3.isConnected())