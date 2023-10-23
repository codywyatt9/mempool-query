from web3.auto import Web3
import asyncio
import logging

# Load your configuration from an external file
wss = 'wss://bold-sly-resonance.quiknode.pro/aa862642de3dcdad72ab18e5ac7c6babfaec8461/'
poll_interval = 2  # You can configure this as needed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name)

web3 = Web3(Web3.WebsocketProvider(wss))

def handle_event(event):
    try:
        transaction = Web3.toJSON(event).strip('"')
        transaction = web3.eth.get_transaction(transaction)
        logger.info(transaction)
    except Exception as err:
        logger.error(f'Error handling event: {err}')

async def log_loop(event_filter):
    while True:
        try:
            for event in event_filter.get_new_entries():
                handle_event(event)
            await asyncio.sleep(poll_interval)
        except Exception as err:
            logger.error(f'Error in log_loop: {err}')

def main():
    tx_filter = web3.eth.filter('pending')
    try:
        asyncio.run(log_loop(tx_filter))
    except KeyboardInterrupt:
        logger.info("Script terminated by user.")

if __name__ == '__main__':
    main()
