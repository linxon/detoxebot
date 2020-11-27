def execute(bot_api):
	bot = bot_api.get()

	@bot.message_handler(func=lambda message: True)
	def echo_message(message):
		bot.reply_to(message, message.text)
