import random, os

TRIGGERED_AT=".*(!слоган|!slogan).*"
PLUGIN_DIR=os.path.dirname(__file__) + '/data/'
DICT_FILE=PLUGIN_DIR + 'slogan.txt'

class Slogan:
	def get_rand_line(self, file, username):
		try:
			lines = open(file).read().splitlines()
			return (random.choice(lines)) % username
		except IOError:
			print("File '" + file + "' not accessible!")

	def remember_it(self, file, max_count, text, username):
		with open(file, 'a') as f:
			f.write(text + '\n')

		f.close()

		curr_c=0
		for l in open(file, 'r').readlines():
			curr_c=curr_c + 1
			if curr_c >= max_count:
				os.remove(file)
				break
			if l == text:
				text = self.remember_it(file, max_count, self.get_rand_line(DICT_FILE))

		return text.encode('utf-8')

def execute(bot_api):
	bot = bot_api.get()
	slogan = Slogan()

	if not os.path.exists(PLUGIN_DIR):
		os.makedirs(PLUGIN_DIR)

	@bot.message_handler(regexp=TRIGGERED_AT)
	def send_slogan(message):
		username = message.from_user.first_name

		slog = slogan.remember_it(PLUGIN_DIR + 'last_msg.txt', 
			20, slogan.get_rand_line(DICT_FILE, username), username)

		bot.send_message(message.chat.id, slog)
