from logging.handlers import DEFAULT_SOAP_LOGGING_PORT
import pandas as pd
from utils import dataCartao, query_table, categorizadorGasto, gpt3OpenAI
from configs import *
import datetime as dt
from pprint import pprint as pp
import requests

#Consulta o saldo do Livro Diário
#####################################################################
def consultarSaldoBanco():

    yearMonth = dataCartao()['yearMonth']

    select = "INSIRA SUA QUERY"
    tbLivroDiario_df = query_table(select)

    agrupaYearMonth = tbLivroDiario_df.groupby(by = 'YearMonth')

    somaValorAnual = agrupaYearMonth['ValorCorrigido'].sum().reset_index()

    df = pd.DataFrame(somaValorAnual)

    filtroYearMonth = df['YearMonth'] == int(yearMonth)

    somaValorYearMonth = df.loc[filtroYearMonth,'ValorCorrigido'].apply(lambda x: '%.2f' % x)

    return somaValorYearMonth

#consultarSaldoBanco()
#####################################################################


#Consulta o saldo do VR
#####################################################################
def consultarSaldoVR():
    select = "INSIRA SUA QUERY"
    tbSaldoVR = query_table(select)
    saldoVR = tbSaldoVR['Saldo_VR']

    return saldoVR

#consultarSaldoVR()
#####################################################################


#Lança um gasto
#####################################################################
def lancarGastoSheets(valor,descricao):

    dataLog = str(dt.datetime.now())
    status = "Pendente"
    tipo = "Despesa"
    data = dataCartao()['data']
    print("data:" + data)
    valor = valor
    contaCartao = "Mastercard Nubank"
    categoria = categorizadorGasto(descricao)['categoria']
    descricao = descricao
    recorrencia = 'Variado'
    classificacao = categorizadorGasto(descricao)['classificacao']
    natureza = categorizadorGasto(descricao)['natureza']

    listaNovosLancamentosLivroDiario = [
                                        dataLog,
                                        status,
                                        tipo,
                                        data.replace("'",""),
                                        str(valor).replace(".",","),
                                        contaCartao,
                                        categoria,
                                        descricao,
                                        recorrencia,
                                        classificacao,
                                        natureza
                                    ]
    sheetLivroDiario = client.open("Tutu Money Bud - Gestor").get_worksheet_by_id("INSIRA O ID")
    sheetLivroDiario.insert_row(listaNovosLancamentosLivroDiario,3,value_input_option="user_entered")
    
#lancarGastoSheets(666,'Uber')
#####################################################################


#Handler para pegar o input do usuário
#####################################################################
def lancamento_handler_tutumb(message):
    lancamento = message.text
    bot.send_message(message.chat.id, f"Obrigado! Seu registro entrará no Tutu Money Bud.")

    valor = lancamento.split(",")[0]
    descricao = lancamento.split(",")[1]

    bot.send_chat_action(message.chat.id,"typing")
    
    lancarGastoSheets(valor,descricao)

    bot.send_message(message.chat.id,"Lançamento registrado com sucesso!")

    bot.send_chat_action(message.chat.id,"typing")

    bot.send_message(message.chat.id,"Saldo atualizado: R$"+consultarSaldoBanco())

#####################################################################


#TutuMoneyBot - Envia notificação para o chat TuBoo
#####################################################################
def tutuMoneyBot(saldoBanco,saldoVR):

    #Variáveis da API
    tokenTutuMoneyBot = "INSIRA O ID DO BOT"
    url = f"https://api.telegram.org/bot{tokenTutuMoneyBot}/sendMessage";
    userID = "INSIRA O ID DO USER"

    #bomDiaGPT = gpt3OpenAI("Escreva uma mensagem de bom dia para a amada.")["choices"][0]["text"]

    #message = f"{bomDiaGPT} -- Saldo atual no Nubank (Crédito): {saldoBanco}. Saldo disponível no VR: {saldoVR}."

    #Desativei o GPT-3 em 04/09
    message = f"Saldo atual no Nubank (Crédito): {saldoBanco}. Saldo disponível no VR: {saldoVR}."

    data = {
        "method": "post",
        "chat_id": userID,
        "text": str(message)
    };

    requests.post(url, data)

#tutuMoneyBot()
#####################################################################