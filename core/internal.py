class DetoxeBotInternal:
	def __init__(self):
		self.languge='ru'

	def setup_commands(self):
		@self.bot.message_handler(commands=['ping'])
		def ping_pong_message(message):
			self.bot.reply_to(message, 'понг!')

		@self.bot.message_handler(commands=['start', 'help'])
		def start_message(message):
			self.bot.send_message(message.chat.id, """ Доступные команды:
!совет, !слоган """)

	def execute(self, bot_api):
		self.bot = bot_api.get()

		bot_api.logger().debug("Setup internal commands...")
		return self.setup_commands()

