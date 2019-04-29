import bot.classes.pyTelegramApi as api

def main():
	api.pyTelegramApi.sendMessage_id(api, api.pyTelegramApi.getChatId(api))