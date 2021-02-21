from core import BotHandler
import config

if __name__ == "__main__":
	bot = BotHandler(
		config.DETOXEBOT_TOKEN,
		config.DETOXEBOT_PLUGINS,
		config.DETOXEBOT_LOGFILE,
		config.DETOXEBOT_DEBUG_LEVEL)

	bot.run()
