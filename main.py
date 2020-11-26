from os import environ
from core import BotHandler

plugins = [
	'sovet4ik.Sovet4ik'
]

if __name__ == "__main__":
	bot = BotHandler(environ['DETOXEBOT_TOKEN'], 20, plugins)
	bot.run()
