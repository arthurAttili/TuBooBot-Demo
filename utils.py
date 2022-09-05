# -*- coding: utf-8 -*- 
from calendar import c
import openai
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#Gera o menuzinho maroto
#####################################################################
def gerar_botoes(categoria_menu):

    if categoria_menu == "tutu_money_bud":
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(
            InlineKeyboardButton("Consultar Saldo", callback_data="consultarSaldo"),
            InlineKeyboardButton("Lançar Gasto", callback_data="lancarGasto"),
        )

    if categoria_menu == "lista_mercado":
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(
            InlineKeyboardButton("Consultar Mercado", callback_data="consultarMercado"),
            InlineKeyboardButton("Adicionar Mercado", callback_data="adicionaMercado"),
            InlineKeyboardButton("Concluir Mercado", callback_data="concluirMercado"),
            InlineKeyboardButton("Comados Mercado", callback_data="comandosMercado")
        )

    if categoria_menu == "automacoes_lampada":
        markup = InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(
            InlineKeyboardButton("Hora do Trabalho", callback_data="horaDoTrabalho"),
            InlineKeyboardButton("Hora do Café", callback_data="horaDoCafe"),
            InlineKeyboardButton("Hora do Jogo", callback_data="horaDoJonas"),
            InlineKeyboardButton("Hora do Dino", callback_data="horaDoDino"),
            InlineKeyboardButton("Boa Noite", callback_data="boaNoite"),
            InlineKeyboardButton("Arthur Dormir", callback_data="oArthurVaiDormir"),
            InlineKeyboardButton("Trabalho Escritório", callback_data="trabalhoEscritorio")
        )

    if categoria_menu == "demais_automacoes":
        markup = InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(
            InlineKeyboardButton("Toggle TV", callback_data="toggleTv"),
            InlineKeyboardButton("Toggle Led TV", callback_data="toggleLedTv"),
            InlineKeyboardButton("Toggle Ventilador", callback_data="toggleVentilador"),
            InlineKeyboardButton("Toggle Quintal", callback_data="toggleQuintal")
        )
    return markup
#####################################################################



#Funcao para fazer query em tabelas do BQ
#####################################################################
def envia_menu(message):
    bot.send_message(message.chat.id,"💰 Interacões com o Tutu Money Bud 💰",reply_markup=gerar_botoes("tutu_money_bud"))
    bot.send_message(message.chat.id,"-")
    bot.send_message(message.chat.id,"🛍️ Listas de mercado 🛍️",reply_markup=gerar_botoes("lista_mercado"))
    bot.send_message(message.chat.id,"-")
    bot.send_message(message.chat.id,"💡 Automações Yeelight 💡",reply_markup=gerar_botoes("automacoes_lampada"))
    bot.send_message(message.chat.id,"-")
    bot.send_message(message.chat.id,"🤖 Demais automações 🤖",reply_markup=gerar_botoes("demais_automacoes"))
#####################################################################

#Funcao para fazer query em tabelas do BQ
#####################################################################
from configs import *
import pandas_gbq

def query_table(query):
    #encoding: utf-8
    #project_id gcp_credentials -- Já configuradas em configs.py
    """
    Requisita uma tabela do BigQuery | Realiza uma consulta

    Args:
        query (string): Consulta que será realizada no BigQuery
        project_id (string): Id do projeto a qual a tabela pertence
        gcp_credentials (client credentials object): Credenciais autenticadas da conta de servico
    Returns:
        dataframe: pandas dataframe com o retorno da consulta
    """
    print("-------------------------------------------")
    print("A funcao query_table foi chamada!")
    print(query)
    print("-------------------------------------------")

    df = pandas_gbq.read_gbq(query, project_id=project_id,
                            credentials=gcp_credentials)
    return (df)
#####################################################################


#Determina a data do cartao. Retorna yearMonth e data
#####################################################################
def dataCartao():
    #encoding: utf-8
    import datetime as dt

    #Determina qual será o YearMonth consultado de acordo com o fechamento da fatura.
    diaHoje = int(dt.datetime.today().strftime("%d"))
    if(diaHoje>=8):
        dataTrintaDias = dt.datetime.today() + dt.timedelta(days=25)
        yearMonth = str(int(dataTrintaDias.strftime("%Y%m")))

        year = yearMonth[:4]
        month = yearMonth[4:]
        data = f"15/{month}/{year}"
        #print(f'yearMonth: {yearMonth} -- data: {data}')
    else:
        yearMonth = str(int(dt.datetime.today().strftime("%Y%m")))
        year = yearMonth[:4]
        month = yearMonth[4:]
        data = f"15/{month}/{year}"
        #print(f'yearMonth: {yearMonth} -- data: {data}')
    
    dicData = {
                'data':data,
                'yearMonth':yearMonth
            }
    
    return dicData

#dataCartao()
#####################################################################


#Determina a categoria do lancamento
#####################################################################
def categorizadorGasto(descricao):
    #encoding: utf-8
    descricao = descricao.lower()

    dicionario_categoria_classificacao_natureza = {
        "uber":"Uber/99_Normal_Manutencao",
        "99":"Uber/99_Normal_Manutencao",

        "chines":"Mercado_Normal_Manutencao",
        "mercado":"Mercado_Normal_Manutencao",
        "feira":"Mercado_Normal_Manutencao",
        "chocolandia":"Mercado_Normal_Manutencao",

        "farmacia":"Farmácia/Saúde_Normal_Manutencao",
        "médico":"Farmácia/Saúde_Essencial_Saúde",
        "goya":"Farmácia/Saúde_Essencial_Saúde",

        "banho dino":"Animais_Normal_Manutencao",
        "petz":"Animais_Normal_Manutencao",

        "bar":"Roles_Normal_Experiencias",
        "pizza":"Rangos_Essencial_Experiencias",
        "papi pizza":"Rangos_Essencial_Experiencias",

        "estacionamento":"Carro_Normal_Manutencao",
        "estacionamento mooca":"Carro_Normal_Manutencao",
        "estacionamento shopping":"Carro_Normal_Manutencao",
        "gasolina":"Carro_Normal_Manutencao",
        "gasolina uno":"Carro_Normal_Manutencao",

        "soho":"Moda_Normal_Manutencao",
        "cabeleireiro":"Moda_Normal_Manutencao",
        "cabelereiro soho":"Moda_Normal_Manutencao",

        "tbb":"Investimentos -- TBB_Investimentos_Investimentos"  
    }

    try:
        categoria = dicionario_categoria_classificacao_natureza[descricao].split("_")[0]
        classificacao = dicionario_categoria_classificacao_natureza[descricao].split("_")[1]
        natureza = dicionario_categoria_classificacao_natureza[descricao].split("_")[2]
    except: 
        categoria = "A Definir"
        classificacao = "A Definir"
        natureza = "A Definir"

    dicionarioCategorizado = {
                        'categoria':categoria,
                        'classificacao':classificacao,
                        'natureza':natureza
                        }

    return dicionarioCategorizado

#print(categorizador("UBER"))
#####################################################################


#Determina a categoria do ítem de mercado
#####################################################################
def categorizadorMercado(item):
    #encoding: utf-8
    item = item.lower()
    
    planilhaListaMercado = client.open("TuBooBot | Lista Mercado").get_worksheet_by_id(0)
    dicionario_sheets_raw = planilhaListaMercado.get_values("F2:F")
    dicionario_sheets = {}

    for i in range(len(dicionario_sheets_raw)):
        lancamento_lista_raw = str(dicionario_sheets_raw[i][0]).replace('"',"")
        lancamento_lista_key = lancamento_lista_raw.split(":")[0].replace("'","")
        lancamento_lista_value = lancamento_lista_raw.split(":")[1].replace("'","")

        dicionario_sheets.update({lancamento_lista_key:lancamento_lista_value})

    try:
        categoria = dicionario_sheets[item].split("_")[0]
        marca = dicionario_sheets[item].split("_")[1]
        valorEstimado = float(dicionario_sheets[item].split("_")[2])
    except: 
        categoria = "-"
        marca = "-"
        valorEstimado = 0

    dicionarioCategorizadoMercado = {
                        'categoria':categoria,
                        'marca':marca,
                        'valorEstimado':valorEstimado
                        }

    return dicionarioCategorizadoMercado 

#categorizadorMercado('nuggets')
#####################################################################


#Bate na API do GPT-3 e dá bom dia
#####################################################################
def gpt3OpenAI(prompt):
    openai.api_key = "INSIRA O TOKEN AQUI";
    
    #prompt = "Escreva uma mensagem de bom dia para a amada."

    completion = openai.Completion.create(
            prompt = prompt,
            engine="text-davinci-002",
            max_tokens=500, 
            temperature=0.7,
            top_p=1,
            n=1,
            stream= False,
            #logprobs=NULL,
            stop=""
        )

    return completion

#print(gpt3OpenAI())
#####################################################################


#Bate na API do Google Drive e baixa um arquivo
#####################################################################
def driveFileDownloader(file_id):
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload
    from google.oauth2 import service_account
    import io

    credentials = service_account.Credentials.from_service_account_info(auth_info)
    drive_service = build('drive', 'v3', credentials=credentials)

    request = drive_service.files().get_media(fileId=file_id)
    #fh = io.BytesIO() # this can be used to keep in memory
    fh = io.FileIO('file.tar.gz', 'wb') # this can be used to write to disk
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
        
#driveFileDownloader('1WPNDo52tnAgrhIZe3G8_Tv__m7hCH8Sx')
#####################################################################