import telegram

chat_bot = telegram.Bot(token='698291638:AAHDFAygbqK_SLCiW6n_Rtbalpt1ogjhIsU')
chat_id = 286510669

chat_bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
