import config
from functions.base import read_json, write_json, update_dict, touch


def create_files():
    touch(path=config.FILES_DIR)
    touch(path=config.WALLETS_FILE, file=True)

    try:
        current_settings: dict | None = read_json(path=config.SETTINGS_FILE)
    except Exception:
        current_settings = {}

    settings = {
        'okx': {
            'required_minimum_balance': 0.001,
            'withdraw_amount': {'from': 0.006, 'to': 0.007},
            'delay_between_withdrawals': {'from': 1200, 'to': 1500},
            'credentials': {
                'api_key': '',
                'secret_key': '',
                'passphrase': '',
            }
        },
        'oklink_api_key': '',
        'minimal_balance': 0.0005
    }
    write_json(path=config.SETTINGS_FILE, obj=update_dict(modifiable=current_settings, template=settings), indent=2)


create_files()