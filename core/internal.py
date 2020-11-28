class DetoxeBotInternal:
	def __init__(self):
		self.languge='ru'

	def execute(self, bot_api):
		self.bot = bot_api.get()

		@self.bot.message_handler(commands=['ping'])
		def start_message(message):
			self.bot.reply_to(message, 'понг!')

		@self.bot.message_handler(commands=['start', 'help'])
		def start_message(message):
			self.bot.send_message(message.chat.id, """ Доступные команды:
совет, слоган """)

		# @self.bot.message_handler(commands=['halt', 'stop'])
		# def stop_me(message):
		# 	self.bot.send_message(message.chat.id, 'Ладно! Всем пока, пацаны!')
		# 	quit()
