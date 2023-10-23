from web3.auto import Web3
import asyncio
import logging
import os

# Load your configuration from an external file or environment variables
wss = os.getenv('ETHEREUM_WS_URL', 'wss://your-ethereum-node-url')
poll_interval = int(os.getenv('POLL_INTERVAL', 2))
log_level = os.getenv('LOG_LEVEL', 'INFO')

# Configure logging
logging.basicConfig(level=log_level)
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
