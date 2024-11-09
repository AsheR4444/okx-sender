import os
import sys
from pathlib import Path

from loguru import logger
from dotenv import load_dotenv

load_dotenv()

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.absolute()

FILES_DIR = os.path.join(ROOT_DIR, 'files')
SETTINGS_FILE = os.path.join(FILES_DIR, 'settings.json')
WALLETS_FILE = os.path.join(FILES_DIR, 'wallets.txt')



LOG_FILE = os.path.join(FILES_DIR, 'log.log')
ERRORS_FILE = os.path.join(FILES_DIR, 'errors.log')

logger.add(ERRORS_FILE, level='ERROR')
logger.add(LOG_FILE, level='INFO')