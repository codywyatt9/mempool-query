from web3.auto import Web3
import asyncio
import json

# input your web socket node credentials in this field.
# this will allow us to stream transactions
wss = 'wss://bold-sly-resonance.quiknode.pro/aa862642de3dcdad72ab18e5ac7c6babfaec8461/'
web3 = Web3(Web3.WebsocketProvider(wss))

print(web3.isConnected())


def handle_event(event):
    # print the transaction hash
    # print(Web3.toJSON(event))

    # use a try / except to have the program continue if there is a bad transaction in the list
    try:
        # remove the quotes in the transaction hash
        transaction = Web3.toJSON(event).strip('"')
        # use the transaction hash that we removed the '"' from to get the details of the transaction
        transaction = web3.eth.get_transaction(transaction)
        # print the transaction and its details
        print(transaction)

    except Exception as err:
        # print transactions with errors. Expect to see transactions people submitted with errors 
        print(f'error: {err}')
