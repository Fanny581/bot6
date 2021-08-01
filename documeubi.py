import telebot # importamos la libreria de telebot
bot = telebot.TeleBot('1922672818:AAFlwQQ6h1HFkrt8N9rFtZbkFV1OC7WLpSA') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()
@bot.message_handler(commands=['documento', 'pdf'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    document = open('C:/Users/Dios es Amor/Desktop/exa/escritura normalizada 2.pdf', 'rb')
    bot.send_document(id, document)
@bot.message_handler(commands=['ubicacion'])
def ubicacion(mensaje):
    bot.send_chat_action(id, 'find_location')
    bot.send_location(id, 15.436097, -87.918103)
bot.polling()