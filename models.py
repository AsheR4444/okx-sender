from dataclasses import dataclass

from config import SETTINGS_FILE
from functions.base import read_json
from libs.py_okx_async.models import OKXCredentials

class AutoRepr:
    """Contains a __repr__ function that automatically builds the output of a class using all its variables."""

    def __repr__(self) -> str:
        values = ('{}={!r}'.format(key, value) for key, value in vars(self).items())
        return '{}({})'.format(self.__class__.__name__, ', '.join(values))


class Singleton:
    """A class that implements the singleton pattern."""
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls)

        return cls._instances[cls]

@dataclass
class FromTo:
    from_: int | float
    to_: int | float

class OkxModel:
    withdraw_amount: FromTo
    delay_between_withdrawals: FromTo
    credentials: OKXCredentials
    maxFee: float | bool

class Settings(Singleton, AutoRepr):
    def __init__(self):
        json_data = read_json(path=SETTINGS_FILE)

        self.okx = OkxModel()
        # self.okx.required_minimum_balance = json_data['okx']['required_minimum_balance']
        self.okx.withdraw_amount = FromTo(
            from_=json_data['okx']['withdraw_amount']['from'],
            to_=json_data['okx']['withdraw_amount']['to'],
        )
        self.okx.delay_between_withdrawals = FromTo(
            from_=json_data['okx']['delay_between_withdrawals']['from'],
            to_=json_data['okx']['delay_between_withdrawals']['to'],
        )
        self.okx.credentials = OKXCredentials(
            api_key=json_data['okx']['credentials']['api_key'],
            secret_key=json_data['okx']['credentials']['secret_key'],
            passphrase=json_data['okx']['credentials']['passphrase']
        )

        self.okx.maxFee = json_data['okx']['max_fee']
        self.oklink_api_key: str = json_data['oklink_api_key']