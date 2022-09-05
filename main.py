# -*- coding: utf-8 -*- 
from configs import *
from utils import *
from mercado import *
from tutuMoneyBud import *
from funcoesYeelight import *
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


#Ações que devem ser realizadas pelos comandos
#####################################################################

#Tutu MB
#############################
def consultar_saldo(call):
    bot.send_message(call.message.chat.id,'Você selecionou a opção Consultar Saldo! Calculando o orçamento disponível...',parse_mode='html')
    bot.send_chat_action(call.message.chat.id,"typing")

    saldoBanco = consultarSaldoBanco()[0]
    saldoVR = consultarSaldoVR()[0]

    bot.send_message(call.message.chat.id,f"Limite do Cartão de Crédito: R${saldoBanco}")
    bot.send_message(call.message.chat.id,f"Saldo no VR: {saldoVR}")
    bot.send_message(call.message.chat.id,"Enviando informação ao chat TuBoo")
    bot.send_chat_action(call.message.chat.id,"typing")
    tutuMoneyBot(saldoBanco,saldoVR)

def lancar_gasto(call):
    mensagemBot = bot.send_message(call.message.chat.id,'Você selecionou a opção Lançar Gasto! Por favor, digite o gasto no seguinte padrão: 42.13,uber')
    bot.register_next_step_handler(mensagemBot, lancamento_handler_tutumb) 
#############################


#Mercado
#############################
def consultar_mercado(call):
    bot.send_message(call.message.chat.id,"Buscando os dados no Big Query.")
    bot.send_chat_action(call.message.chat.id,"typing")
    resultado_lista_consulta = consultarMercado()
    if resultado_lista_consulta == "Lista de mercado vazia!":
        bot.send_message(call.message.chat.id, "Lista de mercado vazia!")
    else:
        url_imagem = r"C:\Users\EXAMPLE\Desktop\TuBooBot-Demo\listaMercado.png"
        
        bot.send_photo(call.message.chat.id,open(url_imagem,"rb"))
        valorMercado = valorTotalMercado()[0]
        bot.send_message(call.message.chat.id, f"Valor total estimado: R${valorMercado}")

def adicionar_mercado(call):
    mensagemBot = bot.send_message(call.message.chat.id,'Você selecionou a opção Adicionar Mercado! Por favor, digite o ítem e a qtd (se for acima de 1). Ex: Nuggets,2')
    bot.register_next_step_handler(mensagemBot, lancamento_handler_mercado_adicionar)
    

def concluir_mercado(call):
    mensagemBot = bot.send_message(call.message.chat.id,'Para marcar todos os ítens da lista como Comprados digite "tudo". Caso queira marcar um ítem da lista, digite exatamente o nome deles (como está na lista). Ex: pizza,banana,melão')
    bot.register_next_step_handler(mensagemBot, lancamento_handler_mercado_concluir) 

def comandos_mercado(call):
    bot.send_message(call.message.chat.id,'Segue a lista de comandos para incluir compras. Digite exatamente o nome deles (como está na lista) para que a classificação seja automática.')
    bot.send_chat_action(call.message.chat.id,"typing")
    bot.send_message(call.message.chat.id, comandosMercado())
#############################


#Luzes
#############################
def hora_do_cafe(call):
    bot.send_message(call.message.chat.id,horaDoCafe_yeelight())

def hora_do_jogo(call):
    bot.send_message(call.message.chat.id,horaDoJogo_yeelight())

def hora_do_dino(call):
    bot.send_message(call.message.chat.id,horaDoDino_yeelight())

def hora_do_trabalho(call):
    bot.send_message(call.message.chat.id,horaDoTrabalho_yeelight())

def boa_noite(call):
    bot.send_message(call.message.chat.id,boaNoite_yeelight())

def arthur_dormir(call):
    bot.send_message(call.message.chat.id,arthurDormir_yeelight())

def trabalho_escritorio(call):
    bot.send_message(call.message.chat.id,trabalhoEscritorio_yeelight())
#############################



#Acionador Inicial
#####################################################################
@bot.message_handler(content_types=["text"])
def responder(message):
    chat_id_1 = "INSIRA O ID AQUI"
    chat_id_2 = "INSIRA O ID AQUI"
    #print(message) #Útil para debugar
    if message.chat.id == chat_id_1 or message.chat.id == chat_id_2:
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        textoEntrada = f'Olá, <b>{first_name} {last_name}</b>! Tudo bom? Escolha um comando para continuar!'
        bot.reply_to(message,textoEntrada,parse_mode='html')
        
        envia_menu(message)

    else:
        texto = "Você não é o Tutu ou a Carol!! Saia já daqui!"
        bot.reply_to(message,texto)
#####################################################################



#Acionador Funções
#####################################################################
@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == "consultarSaldo":
        consultar_saldo(call)

    if call.data == "lancarGasto":
        lancar_gasto(call)

    if call.data == "consultarMercado":
        consultar_mercado(call)

    if call.data == "adicionaMercado":
        adicionar_mercado(call)

    if call.data == "concluirMercado":
        concluir_mercado(call)

    if call.data == "comandosMercado":
        comandos_mercado(call)

    if call.data == "horaDoTrabalho":
        bot.answer_callback_query(call.id, "Hora do Trabalho Ativado!")
        hora_do_trabalho(call)

    if call.data == "horaDoCafe":
        bot.answer_callback_query(call.id, "Hora do Café Ativado!")
        hora_do_cafe(call)

    if call.data == "horaDoJogo":
        bot.answer_callback_query(call.id, "Hora do Jogo Ativado!")
        hora_do_jogo(call)

    if call.data == "horaDoDino":
        bot.answer_callback_query(call.id, "Hora do Dino Ativado!")
        hora_do_dino(call)

    if call.data == "boaNoite":
        bot.answer_callback_query(call.id, "Boa Noite Ativado!")
        boa_noite(call)

    if call.data == "oArthurVaiDormir":
        bot.answer_callback_query(call.id, "Arthur Dormir Ativado!")
        arthur_dormir(call)

    if call.data == "trabalhoEscritorio":
        bot.answer_callback_query(call.id, "Trabalho Escritório Ativado!")
        trabalho_escritorio(call)

    if call.data == "toggleTv":
        bot.answer_callback_query(call.id, "Função em construção!")
        lancar_gasto(call)
#####################################################################


#Ativa o bot.
#bot.polling()
bot.infinity_polling(timeout=10, long_polling_timeout = 5)