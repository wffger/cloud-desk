import logging
from dynaconf import Dynaconf
from fastapi.templating import Jinja2Templates

env = Dynaconf(
  settings_files=['settings/conts.toml', 'settings/.secrets.toml']
  )

# Set up our logger
match env.LOG_LEVEL.upper():
    case 'DEBUG':
        LOG_LVL=logging.DEBUG
    case 'INFO':
        LOG_LVL=logging.INFO
    case 'WARNING':
        LOG_LVL=logging.WARNING
    case 'ERROR':
        LOG_LVL=logging.ERROR
    case 'CRITICAL':
        LOG_LVL=logging.CRITICAL
    case _:
        LOG_LVL=logging.NOTSET
logging.basicConfig(level=LOG_LVL)
logger = logging.getLogger()

# jinja2 template
templates = Jinja2Templates(directory="frontend/templates")