import telebot as tb
import logging

class DetoxeBot:
	def __init__(self, token, logfile, debug_level):
		self.logfile = logfile
		self.debug_level = debug_level

		self.bot = tb.TeleBot(token, parse_mode=None)

		self.log = tb.logger
		self.log.setLevel(self.debug_level)

		log_fh = logging.FileHandler(self.logfile, "w")
		log_fh.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
		self.log.addHandler(log_fh)

	def _loop(self, interval, timeout):
		self.bot.polling(none_stop=True, interval=interval, timeout=timeout)

	def _set_proxy(self, params):
		tb.apihelper.proxy = params

	def get_updates(self, offset, limit, timeout):
		return self.bot.get_updates(offset, limit, timeout)

	def logger(self):
		return self.log

	def get(self):
		return self.bot

