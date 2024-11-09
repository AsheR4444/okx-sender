import random
import time

from actions import OKXActions
from functions.base import randfloat
from libs.py_okx_async.models import Chains
from models import Settings
from loguru import logger

async def okx_withdraw(wallets: list[str]):
    settings = Settings()
    okx = OKXActions(credentials=settings.okx.credentials)

    for num, wallet in enumerate(wallets, start=1):
        logger.info(f'{num}/{len(wallets)} wallets')

        amount_to_withdraw = randfloat(
            from_=settings.okx.withdraw_amount.from_,
            to_=settings.okx.withdraw_amount.to_,
            step=0.0000001
        )

        res = await okx.withdraw(
            to_address=str(wallet),
            amount=amount_to_withdraw,
            token_symbol='ETH',
            chain=Chains.ArbitrumOne
        )

        if 'Failed' not in res:
            logger.success(f'{wallet}: {res}')
            if num >= len(wallets):
                logger.success(f'OKX withdraw successfully completed with {len(wallets)} wallets')
                return

            time.sleep(random.randint(
                settings.okx.delay_between_withdrawals.from_, settings.okx.delay_between_withdrawals.to_))
        else:
            logger.error(f'{wallet}: {res}')
