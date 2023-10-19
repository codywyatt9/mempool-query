from web3.auto import Web3
import asyncio
import json

wss = 'wss://bold-sly-resonance.quiknode.pro/aa862642de3dcdad72ab18e5ac7c6babfaec8461/'
web3 = Web3(Web3.WebsocketProvider(wss))

# Check to see if you are connected to your node
print(web3.isConnected())

router = web3.toChecksumAddress('EnterUniswapOrPancakeSwapRouterAddressHere')

def handle_event(event, router):
    try:
        web3 = Web3() 
        transaction_hash = event.get('transactionHash')
        if not transaction_hash:
            print("Invalid event data: missing transactionHash")
            return
        transaction = web3.eth.getTransaction(transaction_hash)
        if not transaction:
            print(f"Transaction not found for hash: {transaction_hash}")
            return
        to = transaction['to']
        if to == router:
            print(transaction)
        else:
            print('Not what we are looking for')
    except Exception as err:
        print(f'Error: {err}')


async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)

def main():
    # filter for pending transactions
    tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()

