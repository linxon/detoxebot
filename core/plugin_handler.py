import importlib
from core.internal import DetoxeBotInternal as internal_commands

class PluginMountingFailure(Exception):
    pass

class PluginHandler:
	def __init__(self, *, plugins: list=list()):
		self.internal_modules = [ internal_commands() ]
		self.external_modules = plugins

	def load_plugin(self, name):
		try:
			return importlib.import_module(name)
		except(ModuleNotFoundError or AttributeError):
			return None

	def call_plugins(self, bot_api):
		for module in self.internal_modules:
			module.execute(bot_api)

		for module in self.external_modules:
			plugin = self.load_plugin(module)
			if plugin is not None:
				plugin.execute(bot_api)
			else:
				bot_api.logger().info("module: %s - is not available!" % module)
