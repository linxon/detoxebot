from os import environ
from core import BotHandler

################################################

DETOXEBOT_TOKEN = environ['DETOXEBOT_TOKEN']
DETOXEBOT_PLUGINS = [ 'plugins.sovet4ik', 'plugins.slogan' ]
DETOXEBOT_INTERVAL = 3
DETOXEBOT_TIMEOUT = 20

################################################

if __name__ == "__main__":
	bot = BotHandler(
		DETOXEBOT_TOKEN,
		DETOXEBOT_INTERVAL,
		DETOXEBOT_TIMEOUT,
		DETOXEBOT_PLUGINS)

	bot.bot_api.set_debug(1)
	# bot.bot_api.set_proxy({
	# 	'http':'http://10.10.1.10:3128',
	# 	'https':'socks5://userproxy:password@proxy_address:port'
	# })

	bot.run()
