

import requests
from tkinter import*

def pegar_cotacao():
    requisicao = requests.get("http://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    
    rqs = requisicao.json()
    dolarAtual = rqs['USDBRL']['bid']
    euroAtual = rqs['EURBRL']['bid']
    btcAtual = rqs['BTCBRL']['bid']

    texto = f'''
        DOLAR: {dolarAtual}
        EURO: {euroAtual}
        BTC: {btcAtual}'''
    
#pegar_cotacao()

    #print(texto)
    texto_resposta["text"] = texto

    def limpar():
        texto_resposta["text"] = " "

janela = Tk()
janela.geometry("200x200")
janela.title("Cotação atual das moedas")
texto = Label(janela, text = "Clique no botão para exibir as cotações")
texto.grid(column = 0, row = 0, padx = 10, pady = 10)

botao = Button(janela, text = "Buscar cotações", command = pegar_cotacao)
botao.grid(column = 0, row = 1, padx = 10, pady = 10)
texto_resposta = Label(janela, text = " ")
texto_resposta.grid(column = 0, row = 2, padx = 10, pady = 10)

janela.mainloop() 