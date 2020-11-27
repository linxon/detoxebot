import telebot

class DetoxeBot:
	def __init__(self, token, timeout):
		self.timeout = timeout
		self.bot = telebot.TeleBot(token)

	def get(self):
		return self.bot

	def loop(self):
		self.bot.polling(none_stop=True, interval=0, timeout=self.timeout)

