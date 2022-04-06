import json
import sys
import os

class Chatbot():
    def __init__(self,nome):
        try:
            memoria=open(nome+'.json','r')
        except FileNotFoundError:
            memoria=open(nome+'.json','w')
            memoria.write('[["fellipe","joao"],{"oi":"Olá, qual o seu nome?","tchau":"tchau,tchau"}]')
            memoria.close()
            memoria=open(nome+'.json','r')
            
        self.nome=nome
        self.conhecidos,self.frases=json.load(memoria)
        memoria.close()
        self.criador=['winicius','Winicius', 'João Winicius']
        self.historico=[None,]

    def escuta(self,frase=None):
        if frase == None:
            frase=input ('>: ')
        frase=str(frase)
        frase=frase.lower()
        frase=frase.replace('é','eh')
        return frase

    def pensa(self,frase):
        if frase in self.frases:
            return self.frases[frase]
        if frase=='aprende':
            return 'Digite a frase: '

        #responde frase que depende do histórico
        ultimafrase=self.historico[-1]
        if ultimafrase == 'Olá, qual o seu nome?':
            nome=self.peganome(frase)
            resp=self.respnome1(nome)
            return resp
        if ultimafrase == 'Digite a frase: ':
            self.chave=frase
            return 'Digite a resposta: '
        if ultimafrase == 'Digite a resposta: ':
            resp=frase
            self.frases[self.chave]=resp
            self.gravamemoria()
            return 'A informação  foi salva no meu banco de dados!'

        if frase == 'desliga':
            self.desligar=os.system('shutdown -s')
            return 'desligando tudo!'

        try:
            resp=str(eval(frase))
            return resp
        except:
            pass
        return 'Nao entendi'

    def peganome(self,nome):
        if 'o meu nome eh' in nome:
            nome=nome[14:]

        nome=nome.title()
        return nome

    #resposta de nome criador
    def respnome1(self,nome):
        if nome in self.criador:
            resp='olá senhor Universo!'
            return resp
        if nome in self.conhecidos:
            resp='Iae, que bom ver você por aqui novamente '
        else:
            resp='Muito prazer '
            self.conhecidos.append(nome)
            self.gravamemoria()
        return resp+nome+'!'

    def gravamemoria(self): 
        memoria=open(self.nome+'.json','w')
        json.dump([self.conhecidos,self.frases],memoria)
        memoria.close()

    def fala(self,frase):
        if 'executa ' in frase:
            plataforma=sys.platform
            comando=frase.replace('executa ','')
            if 'win' in plataforma:
                os.startfile(comando)
        else:
            print(frase)
        self.historico.append(frase)
       

   
