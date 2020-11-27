class DetoxeBotInternal:
	def __init__(self):
		self.test = 1

	def execute(self, bot_api):
		self.bot = bot_api.get()

		@self.bot.message_handler(commands=['start', 'help'])
		def start_message(message):
			self.bot.send_message(message.chat.id, 'Хуле надо?')
