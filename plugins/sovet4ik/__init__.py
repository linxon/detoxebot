import random, os, time

TRIGGERED_AT=".*(совет|sovet|advice).*"
PLUGIN_DIR=os.path.dirname(__file__) + '/data/'

def get_rand_line(file):
	lines = open(file).read().splitlines()
	return random.choice(lines)

def remember_it(file, max_count, text):
	return text

def execute(bot_api):
	bot = bot_api.get()

	@bot.message_handler(regexp=TRIGGERED_AT)
	def send_advice(message):
		time.sleep(2)

		msg = remember_it(PLUGIN_DIR + 'last_msg.txt', 5, get_rand_line(PLUGIN_DIR + 'sovet.txt'))
		bot.reply_to(message, msg)
