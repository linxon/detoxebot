import random, os

TRIGGERED_AT=".*(!совет|!sovet)+"
PLUGIN_DIR=os.path.dirname(__file__) + '/data/'
DICT_FILE=PLUGIN_DIR + 'sovet.txt'

if not os.path.exists(PLUGIN_DIR):
	os.makedirs(PLUGIN_DIR)

class Sovet4ik:
	def get_rand_adv(self):
		try:
			lines = open(DICT_FILE).read().splitlines()
			return random.choice(lines)
		except IOError:
			print("File '" + DICT_FILE + "' not accessible!")

	def get_count_num(self, file):
		return int(len(open(DICT_FILE, 'r').readlines()) / 100 * 30)

	def remember_it(self, text):
		file = PLUGIN_DIR + 'last_msg.txt'
		max_count = self.get_count_num(file)

		with open(file, 'a') as f:
			f.write(text + '\n')

		f.close()

		curr_c=0
		for l in open(file, 'r').readlines():
			print(l.rstrip("\n") + ' == ' + text)
			curr_c=curr_c + 1
			if curr_c >= max_count:
				os.remove(file)
				break
			if l.rstrip("\n") == text:
				text = self.remember_it(self.get_rand_adv())
			else:
				break

		return text.encode('utf-8')

def execute(bot_api):
	bot = bot_api.get()
	sovet4ik = Sovet4ik()

	@bot.message_handler(regexp=TRIGGERED_AT)
	def send_advice(message):
		bot_api.logger().debug("sovet4ik: sending message...")
		bot.reply_to(message, sovet4ik.remember_it(sovet4ik.get_rand_adv()))
