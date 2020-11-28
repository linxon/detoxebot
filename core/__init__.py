from core.detoxebot import DetoxeBot
from core.plugin_handler import PluginHandler

class BotHandler:
	def __init__(self, token, interval, timeout, plugin_list, debug_level = 0):
		self.bot_api = DetoxeBot(token, interval,
			timeout, debug_level)

		plugin = PluginHandler(plugins=plugin_list)
		plugin.call_plugins(self.bot_api)

	def run(self):
		self.bot_api.loop()

