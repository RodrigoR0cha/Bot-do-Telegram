import requests 
import time 
import json
import os

class TelegramBot:
    def __init__(self):
        token = '5203496122:AAFbM5UBZCA_a1fY9znEk24QT6AoET_nDCU'
        self.url_base = f'api.telegram.org/bot{token}/'  


# método iniciar o bot (None - pq primeira verificação é sempre vazia)
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagens = (update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    eh_primeira_mensagem = mensagem['message']['message_id'] == 1
                    resposta = self.criar_resposta(mensagem,eh_primeira_mensagem)
                    self.responder(resposta,chat_id)

# forma de receber as mensagens 
    def obter_mensagens(self,update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
# forma de criar respostas 
    def criar_resposta(self,mensagem,eh_primeira_mensagem):
       mensagem = mensagem['message']['text']
       if eh_primeira_mensagem == True or mensagem.lower() == 'menu':
           return f'''Olá bem vindo a nossa lanchonete. Digite o número do hamburguer 
           que gostaria de pedir{os.linesep}1 - Queijo MAX{os.linesep}
           2 - Duplu Burguer Bacon{os.linesep} 3 - Triple XXX'''
       if mensagem == '1':
            return f'''Queijo Max - R$20,00{os.linesep}Confirmar pedidos(s/n)'''       
       if mensagem == '2':
            return f'''Duplo Burguer Bacon - R$25,00{os.linesep}Confirmar pedidos(s/n)'''       
       if mensagem == '3':
            return f'''Triple XXX - R$30,00{os.linesep}Confirmar pedidos(s/n)'''       
       if mensagem.lower() in ('s', 'sim'):
           return 'Pedido Confirmado!'
       else:
           return 'Gostaria de acessar o menu? Digite "menu"'    

# Responder
    def responder(self,resposta,chat_id):
    #enviar
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)

#inicializador
bot = TelegramBot()
bot.Iniciar()
