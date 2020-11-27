from core.detoxebot import DetoxeBot
from core.plugin_handler import PluginHandler

class BotHandler:
	def __init__(self, token, timeout, plugin_list):
		self.bot_api = DetoxeBot(token, timeout)

		plugin = PluginHandler(plugins=plugin_list)
		plugin.call_plugins(self.bot_api)

	def run(self):
		self.bot_api.loop()

