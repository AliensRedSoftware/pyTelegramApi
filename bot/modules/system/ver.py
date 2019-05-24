import bot.classes.pyTelegramApi as api

def main():
	api.pyTelegramApi.sendMessage_array(api, ['/start - Возвращаем стэк команд', '/getChatId - Возвращаем chat_id', '/getStickerId -  Возвращаем стикер ид', '/sendSticker - Отправить стикер по ид', '/ava - Отправить аватарку', '/help - Возвращаем стэк команд'])
