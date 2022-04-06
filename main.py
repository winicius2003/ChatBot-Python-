from chatbot import Chatbot

Bot=Chatbot('Zion')
while True:
    frase=Bot.escuta()
    resp=Bot.pensa(frase)
    Bot.fala(resp)
    if frase == 'tchau':
        break
   
      
#fim
