import bot.bot as main

if __name__ == '__main__':
	token = open('token')
	main.main(token.read())