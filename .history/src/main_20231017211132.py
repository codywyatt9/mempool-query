from web3.auto import Web3
import asyncio
import json

# input your web socket node credentials in this field.
# this will allow us to stream transactions
wss = 'wss://bold-sly-resonance.quiknode.pro/aa862642de3dcdad72ab18e5ac7c6babfaec8461/'
web3 = Web3(Web3.WebsocketProvider(wss))

print(web3.isConnected())


def handle_event(event):
    try:
        transaction = Web3.toJSON(event).strip('"')
        transaction = web3.eth.get_transaction(transaction)
        print(transaction)

    except Exception as err: 
        print(f'error: {err}')


async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)