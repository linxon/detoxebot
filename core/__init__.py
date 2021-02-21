from core.detoxebot import DetoxeBot
from core.plugin_handler import PluginHandler

class BotHandler:
	def __init__(self, token, plugin_list, logfile, debug_level = 0):
		self.bot_api = DetoxeBot(token, logfile, debug_level)

		self.bot_api.logger().info("Loading plugins: %s" % plugin_list)
		plugin = PluginHandler(plugins=plugin_list)
		plugin.call_plugins(self.bot_api)

	def run(self, interval = 3, timeout = 20):
		self.bot_api._loop(interval, timeout)

