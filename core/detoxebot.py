import telebot

class DetoxeBot:
	def __init__(self, token, timeout):
		self.timeout = timeout
		self.bot = telebot.TeleBot(token)

		@self.bot.message_handler(content_types=['text'])
		def _send_text_message(message):
			self.send_text_message(message)

	# def get_cmd(self, message):
	# 	return

	def send_text_message(self, message):
		self.channel_id = message.chat.id
		channel_cmd = message.text.lower()

		self.bot.send_message(self.channel_id, channel_cmd)

	def loop_me(self):
		self.bot.polling(none_stop=True, interval=0, timeout=self.timeout)

