import bot.classes.pyTelegramApi as api

def main(token):
	api.pyTelegramApi.setToken(api,token) #Установка токена
	#Команды
	api.pyTelegramApi.addcommand('/getChatId' , 'fun.getChatId')
	api.pyTelegramApi.addcommand('/str' , 'str.str')
	api.pyTelegramApi.addcommand('/getStickerId' , 'sticker.sticker')
	api.pyTelegramApi.addcommand('/sendSticker' , 'sticker.sendSticker')
	api.pyTelegramApi.addcommand('/ava' , 'fun.ava')
	api.pyTelegramApi.addcommand('/start' , 'system.ver')
	#Проверка на правильность токена
	api.pyTelegramApi.checkToken(api.pyTelegramApi.getToken(api)) #Проверка на подлиность токе