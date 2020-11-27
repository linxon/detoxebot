from os import environ
from core import BotHandler

DETOXEBOT_TOKEN = environ['DETOXEBOT_TOKEN']
DETOXEBOT_PLUGINS = [ 'plugins.sovet4ik', 'plugins.echo' ]

if __name__ == "__main__":
	bot = BotHandler(DETOXEBOT_TOKEN, 20, PLUGINS)
	bot.run()
