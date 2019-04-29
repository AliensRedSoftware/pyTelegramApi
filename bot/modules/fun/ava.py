import bot.classes.pyTelegramApi as api
import random

def main():
	api.pyTelegramApi.sendPhoto_ByUrl(api, "https://www.thiswaifudoesnotexist.net/example-{0}.jpg".format(random.randint(0, 99999)))