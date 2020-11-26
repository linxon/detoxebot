import importlib
from core.internal import DetoxeBotInternal

class PluginHandler:
	def __init__(self, *, plugins: list=list()):
		self.internal_modules = [ DetoxeBotInternal() ]
		self.external_modules = plugins

	def load_plugin(self, name):
		try:
			class_data = name.split(".")
			module_path = ".".join(class_data[:-1])
			class_str = class_data[-1]

			module = importlib.import_module("plugins.%s" % module_path)
			return getattr(module, class_str)
		except(ModuleNotFoundError or AttributeError):
			return None

	def call_plugins(self, bot_api):
		for ext_module in self.external_modules:
			plugin = self.load_plugin(ext_module)
			if plugin is not None:
				plugin.process(bot_api)
			else:
				print("Error: plugin '%s' is not available!" % ext_module)

		for module in self.internal_modules:
			module.process(bot_api)
