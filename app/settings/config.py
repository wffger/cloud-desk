from dynaconf import Dynaconf
import logging
from fastapi.templating import Jinja2Templates

env = Dynaconf(
  settings_files=['settings/conts.toml', 'settings/.secrets.toml']
  )

# Set up our logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# jinja2 template
templates = Jinja2Templates(directory="frontend/templates")