#Bibliotecas que um dia poderão ser úteis
#####################################################################
""" 
import pandas as pd
from pandas.io import gbq
import numpy as np
#import google.cloud
#from google.cloud import bigquery
#from oauth2client.client import GoogleCredentials
from google.oauth2 import service_account
import time as tm
import datetime as dt
from datetime import date,timedelta,datetime
"""
#####################################################################




#Autenticação ao Telegram
#####################################################################
import telebot
CHAVE_API = "INSIRA AQUI A CHAVE API DO BOT"
bot = telebot.TeleBot(CHAVE_API)
#####################################################################




#Códigos de autenticação ao GCP.
#####################################################################
from google.oauth2 import service_account
import gspread

auth_info = {
    "type": "service_account",
    "project_id": "1234",
    "private_key_id": "1234",
    "private_key": "1234",
    "client_email": "1234",
    "client_id_antigo": "1234",
    "client_id":"1234",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret":"1234",
    "client_x509_cert_url": "1234"
}

project_id = auth_info['project_id']
gcp_credentials = service_account.Credentials.from_service_account_info(auth_info, 
                                                                        scopes=[
                                                                            "https://www.googleapis.com/auth/cloud-platform",
                                                                            "https://www.googleapis.com/auth/drive",
                                                                            "https://www.googleapis.com/auth/bigquery",
                                                                            "https://spreadsheets.google.com/feeds",
                                                                            'https://www.googleapis.com/auth/spreadsheets',
                                                                            "https://www.googleapis.com/auth/drive.file",
                                                                            "https://www.googleapis.com/auth/photoslibrary",
                                                                            "https://www.googleapis.com/auth/photoslibrary.readonly",
                                                                            "https://www.googleapis.com/auth/photoslibrary.sharing",
                                                                            ],
                                                                        )
client = gspread.authorize(gcp_credentials)
#####################################################################