import random, os

TRIGGERED_AT=".*(совет|sovet|advice).*"
PLUGIN_DIR=os.path.dirname(__file__) + '/data/'
DICT_FILE=PLUGIN_DIR + 'sovet.txt'

class Sovet4ik:
	def get_rand_line(self, file):
		try:
			lines = open(file).read().splitlines()
			return random.choice(lines)
		except IOError:
			print("File '" + file + "' not accessible!")

	def remember_it(self, file, max_count, text):
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
	sovet4ik = Sovet4ik()

	if not os.path.exists(PLUGIN_DIR):
		os.makedirs(PLUGIN_DIR)

	@bot.message_handler(regexp=TRIGGERED_AT)
	def send_advice(message):
		adv = sovet4ik.remember_it(PLUGIN_DIR + 'last_msg.txt', 
			20, sovet4ik.get_rand_line(DICT_FILE))

		bot.reply_to(message, adv)
