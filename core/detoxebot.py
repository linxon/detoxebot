import telebot
import logging

class DetoxeBot:
	def __init__(self, token, interval, timeout, debug_level = 0):
		self.interval = interval
		self.timeout = timeout
		self.set_debug(debug_level)

		self.bot = telebot.TeleBot(token, parse_mode=None)

	def set_debug(self, level = 0):
		if level > 0:
			logger = telebot.logger
			telebot.logger.setLevel(logging.DEBUG)

		self.debug_level = level

	def set_proxy(self, params):
		telebot.apihelper.proxy = params

	def get_updates(self, offset, limit, timeout):
		return self.bot.get_updates(offset, limit, timeout)

	def get(self):
		return self.bot

	def loop(self):
		self.bot.polling(none_stop=True, interval=self.interval, timeout=self.timeout)

