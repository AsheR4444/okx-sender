import asyncio

import config

from loguru import logger

from functions.create_files import create_files
from main import okx_withdraw
from models import Settings

async def start_okx_withdraw():
    settings = Settings()
    
    if not settings.okx.credentials.completely_filled():
        logger.error('OKX credentials not filled')
        return
    with open(config.WALLETS_FILE, "r") as file:
        wallets = file.readlines()

    await okx_withdraw(wallets=wallets)



if __name__ == '__main__':
    create_files()

    asyncio.run(start_okx_withdraw())

