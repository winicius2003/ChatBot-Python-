import telepot
from chatbot import Chatbot
telegram=telepot.Bot ('1179036113:AAE-Iq72DzBbAcjOjtI1uoU5z03aZ4fpepE')
bot=Chatbot ('zion') 

def recebendoMsg(msg):
    frase=bot.escuta(frase=msg['text'])
    resp=bot.pensa(frase)
    bot.fala(resp)
    #chatID=msg['chat']['id']
    tipoMsg, tipoChat, chatID=telepot.glance(msg)
    telegram.sendMessage(chatID,resp)

telegram .message_loop(recebendoMsg)
while True:
    pass
