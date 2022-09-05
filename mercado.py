import datetime as dt
from queue import Empty
from utils import query_table, categorizadorMercado
from configs import *
import unidecode



#Consulta a tabela de forma ordenada e agrupada
#####################################################################
def consultarMercado():
    import dataframe_image as dfi
    #encoding: utf-8
    select = "INSIRA SUA QUERY AQUI" 
    df_query = query_table(select)
    if df_query.empty:
        texto_aviso = "Lista de mercado vazia!"
        return texto_aviso
    else:
        imagem = dfi.export(df_query, 'listaMercado.png')
        return imagem

#consultarMercado()
#####################################################################



#Consulta a tabela de forma ordenada e agrupada
#####################################################################
def valorTotalMercado():
    select = "INSIRA SUA QUERY AQUI" 
    df_query = query_table(select)
    if df_query.empty:
        texto_aviso = "-"
        return texto_aviso
    else:
        return df_query['ValorEstimado'].apply(lambda x: '%.2f' % x)

#valorTotalMercado()
#####################################################################


#Handler para pegar o input do usuário
#####################################################################
def adicionarMercado(item,qtd):

    dataAtualizacao = str(dt.datetime.now())
    item = unidecode.unidecode(item)
    item = item.lower()
    qtd = qtd

    classificador = categorizadorMercado(item)

    categoria = classificador['categoria']
    marca = classificador['marca']
    valorEstimado = classificador['valorEstimado']
    comprar = "Sim"

    if categoria == "A Categorizar":
        listaCompras = f'"{dataAtualizacao}", "{item}", "A Categorizar", "A Categorizar", {qtd}, 0, "{comprar}"'
    else:
        listaCompras = f'"{dataAtualizacao}", "{item}", "{categoria}", "{marca}", {qtd}, {valorEstimado}, "{comprar}"'

    select = "INSIRA SUA QYERY AQUI"
    query_table(select)

#adicionarMercado('cachaça')
#####################################################################


#Handler para pegar o input do usuário
#####################################################################
def lancamento_handler_mercado_adicionar(message):
    
    from mercado import adicionarMercado

    lancamento = message.text

    try:
        item = lancamento.split(",")[0]
        qtd = lancamento.split(",")[1]
    except:
        item = lancamento
        qtd = 1

    item = item.lower()

    bot.send_message(message.chat.id, f"Obrigado! Seu registro será classificado e entrará na lista.")

    bot.send_chat_action(message.chat.id,"typing")
    
    adicionarMercado(item,qtd)

    bot.send_message(message.chat.id,"Ítem registrado com sucesso! Veja como ficou a lista:")

    bot.send_chat_action(message.chat.id,"typing")

    consultarMercado()
    url_imagem = r"C:\Users\EXAMPLE\Desktop\TuBooBot-Demo\listaMercado.png"
    bot.send_photo(message.chat.id,open(url_imagem,"rb"))

    bot.send_message(message.chat.id,"/adicionaMercado")
#####################################################################


#Handler para pegar o input do usuário
#####################################################################
def concluirMercado(item,message):

    item = unidecode.unidecode(item)
    item = item.lower()

    if item == "tudo" or item == "Tudo":
        select = "INSIRA SUA QUERY AQUI"
    else:
        listaItensCru = str(item.split(",")).replace("[","").replace("]","")

        select = "INSIRA SUA QUERY AQUI"

    bot.send_chat_action(message.chat.id,"typing")

    query_table(select)
#####################################################################


#Handler para pegar o input do usuário
#####################################################################
def lancamento_handler_mercado_concluir(message):

    item = message.text
    item = item.lower()

    bot.send_message(message.chat.id, f"O TuBooBot irá registrar a(s) compra(s) e atualizar a lista de mercado.")

    bot.send_chat_action(message.chat.id,"typing")
    
    concluirMercado(item,message)

    bot.send_message(message.chat.id,"Lista atualizada com sucesso!")

#lancamento_handler_mercado_concluir("pizza,banana,melão")
#####################################################################



#Consulta a lista de comandos gravados num sheets
#####################################################################
def comandosMercado():

    planilhaListaMercado = client.open("TuBooBot | Lista Mercado").get_worksheet_by_id(0)
    lista_sheets_raw = planilhaListaMercado.get_values("A2:A")
    listaItens = []

    for i in range(len(lista_sheets_raw)):
        listaItens.append(str(lista_sheets_raw[i][0]).replace('"',""))
    
    resultado_lista_itens = s = ' -- '.join(listaItens)
    return resultado_lista_itens

#print(comandosMercado())
#####################################################################