from os import environ
import logging

DETOXEBOT_TOKEN = environ['DETOXEBOT_TOKEN']
DETOXEBOT_PLUGINS = [ 'plugins.sovet4ik', 'plugins.slogan' ]
DETOXEBOT_INTERVAL = 3
DETOXEBOT_TIMEOUT = 20
DETOXEBOT_DEBUG_LEVEL = logging.INFO
DETOXEBOT_LOGFILE = '/tmp/detoxebot.log'
