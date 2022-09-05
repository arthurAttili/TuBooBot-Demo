from yeelight import Bulb

#Útil para descobrir lâmpadas novas e cores (ele acha o IP e outras infos)
#from yeelight import discover_bulbs
#print(discover_bulbs())

#Colinha marota
#####################################################################
# Turn the bulb on.
#bulb.turn_on()

# Turn the bulb off.
#bulb.turn_off()

# Toggle power.
#bulb.toggle()

# Set brightness to 50%.
#bulb.set_brightness(50)

# Set brightness of the background light to 50%, if your light supports it.
#from yeelight import LightType
#bulb.set_brightness(50, light_type=LightType.Ambient)

# Set RGB value.
#bulb.set_rgb(255, 0, 0)

# Set HSV value.
#bulb.set_hsv(320, 100, 50)

# Set hue and saturation, but keep value (brightness) the same.
#bulb.set_hsv(320, 100)

# Set color temperature.
#bulb.set_color_temp(4700)

# Save this setting as default.
#bulb.set_default()

# Pega as propriedades da lâmpada
#bulb.get_properties()

#bulb_escritorio.set_color_temp(1700) #Menor temperatura possível
#bulb_escritorio.set_color_temp(6500) #Maior temperatura possível
#####################################################################


#Variáveis principais
#####################################################################
#O IP da lâmpada tá disponível dentro do app quando você seleciona a lâmpada e vai em informações.
bulb_escritorio = Bulb('INSIRA IP DA LÂMPADA')
bulb_sala_teto = Bulb('INSIRA IP DA LÂMPADA')
bulb_sala_luminaria = Bulb('INSIRA IP DA LÂMPADA')
bulb_cozinha = Bulb('INSIRA IP DA LÂMPADA')
bulb_quarto = Bulb('INSIRA IP DA LÂMPADA')
bulb_garagem = Bulb('INSIRA IP DA LÂMPADA')
bulb_corredor = Bulb('INSIRA IP DA LÂMPADA')
#####################################################################


#Função para configurar estado branco da lâmpada
#####################################################################
def lampada_branca(nomeLampada,temperatura,brilho):
    nomeLampada.turn_on()
    nomeLampada.set_color_temp(temperatura)
    nomeLampada.set_brightness(brilho)
    #1700 #Menor temperatura possível
    #6500 #Maior temperatura possível
#####################################################################


#Função para configurar estado colorido da lâmpada
#####################################################################
def lampada_colorida(nomeLampada,hue,saturacao,brilho):
    nomeLampada.turn_on()
    nomeLampada.set_hsv(hue, saturacao, brilho)
#####################################################################


#Utilizado para avaliar estados e gerar funções
#####################################################################
""" 
def testes_yeelight():
    print("------------- INICIANDO AVALIACAO -------------")
    print("********** Hora do Dino **********")

    print("--------Corredor-------")
    bulb_avaliado = bulb_corredor
    bulb_avaliado_string = 'bulb_corredor'

    propriedadesBulb = bulb_avaliado.get_properties()
    temperatura = propriedadesBulb['ct']
    brilho = propriedadesBulb['bright']
    hue = propriedadesBulb['hue']
    saturacao = propriedadesBulb['sat']

    print(f'Temperatura: {temperatura}, Brilho: {brilho}, HUE: {hue}, Saturacao: {saturacao}')
    print(f'lampada_branca({bulb_avaliado_string},{temperatura},{brilho})')
    print(f'lampada_colorida({bulb_avaliado_string},{hue},{saturacao},{brilho})')
    
    print("--------Sala Luminaria-------")
    bulb_avaliado = bulb_sala_luminaria
    bulb_avaliado_string = 'bulb_sala_luminaria'

    propriedadesBulb = bulb_avaliado.get_properties()
    temperatura = propriedadesBulb['ct']
    brilho = propriedadesBulb['bright']
    hue = propriedadesBulb['hue']
    saturacao = propriedadesBulb['sat']

    print(f'Temperatura: {temperatura}, Brilho: {brilho}, HUE: {hue}, Saturacao: {saturacao}')
    print(f'lampada_branca({bulb_avaliado_string},{temperatura},{brilho})')
    print(f'lampada_colorida({bulb_avaliado_string},{hue},{saturacao},{brilho})')

    print("-------Sala Teto--------")
    bulb_avaliado = bulb_sala_teto
    bulb_avaliado_string = 'bulb_sala_teto'

    propriedadesBulb = bulb_avaliado.get_properties()
    temperatura = propriedadesBulb['ct']
    brilho = propriedadesBulb['bright']
    hue = propriedadesBulb['hue']
    saturacao = propriedadesBulb['sat']

    print(f'Temperatura: {temperatura}, Brilho: {brilho}, HUE: {hue}, Saturacao: {saturacao}')
    print(f'lampada_branca({bulb_avaliado_string},{temperatura},{brilho})')
    print(f'lampada_colorida({bulb_avaliado_string},{hue},{saturacao},{brilho})')

    print("-------Escritorio--------")
    bulb_avaliado = bulb_escritorio
    bulb_avaliado_string = 'bulb_escritorio'

    propriedadesBulb = bulb_avaliado.get_properties()
    temperatura = propriedadesBulb['ct']
    brilho = propriedadesBulb['bright']
    hue = propriedadesBulb['hue']
    saturacao = propriedadesBulb['sat']

    print(f'Temperatura: {temperatura}, Brilho: {brilho}, HUE: {hue}, Saturacao: {saturacao}')
    print(f'lampada_branca({bulb_avaliado_string},{temperatura},{brilho})')
    print(f'lampada_colorida({bulb_avaliado_string},{hue},{saturacao},{brilho})')
    
    print("--------Cozinha-------")
    bulb_avaliado = bulb_cozinha
    bulb_avaliado_string = 'bulb_cozinha'

    propriedadesBulb = bulb_avaliado.get_properties()
    temperatura = propriedadesBulb['ct']
    brilho = propriedadesBulb['bright']
    hue = propriedadesBulb['hue']
    saturacao = propriedadesBulb['sat']

    print(f'Temperatura: {temperatura}, Brilho: {brilho}, HUE: {hue}, Saturacao: {saturacao}')
    print(f'lampada_branca({bulb_avaliado_string},{temperatura},{brilho})')
    print(f'lampada_colorida({bulb_avaliado_string},{hue},{saturacao},{brilho})')
    
    print("--------Quarto-------")
    bulb_avaliado = bulb_quarto
    bulb_avaliado_string = 'bulb_quarto'

    propriedadesBulb = bulb_avaliado.get_properties()
    temperatura = propriedadesBulb['ct']
    brilho = propriedadesBulb['bright']
    hue = propriedadesBulb['hue']
    saturacao = propriedadesBulb['sat']

    print(f'Temperatura: {temperatura}, Brilho: {brilho}, HUE: {hue}, Saturacao: {saturacao}')
    print(f'lampada_branca({bulb_avaliado_string},{temperatura},{brilho})')
    print(f'lampada_colorida({bulb_avaliado_string},{hue},{saturacao},{brilho})') 
    """

#testes_yeelight()
#####################################################################


#Hora do Café -- Done!
#####################################################################
def horaDoCafe_yeelight():
    try:
        lampada_branca(bulb_corredor,4000,100)
    except:
        ""
    try:
        lampada_branca(bulb_sala_luminaria,2500,100)
    except:
        ""
    try:
        lampada_branca(bulb_sala_teto,3200,100)
    except:
        ""
    try:
        lampada_branca(bulb_escritorio,3150,100)
    except:
        ""
    try:
        lampada_branca(bulb_cozinha,3700,100)
    except:
        ""

#horaDoCafe_yeelight()
#####################################################################


#Hora do Jogo -- Done!
#####################################################################
def horaDoJogo_yeelight():
    try:
        lampada_branca(bulb_corredor,1700,1)
    except:
        ""
    try:
        lampada_colorida(bulb_sala_teto,280,90,40)
    except:
        ""
    try:
        lampada_branca(bulb_sala_luminaria,1775,25)
    except:
        ""
        #quinta_telhado_colorido
    try:
        lampada_branca(bulb_escritorio,2250,100)
    except:
        ""
    try:
        lampada_branca(bulb_quarto,1760,30)
    except:
        ""
    try:
        lampada_branca(bulb_cozinha,2175,100)
    except:
        ""

#horaDoJogo_yeelight()
#####################################################################


#Hora do Dino -- Done!
#####################################################################
def horaDoDino_yeelight():
    try:
        bulb_sala_teto.turn_off()
    except:
        ""
    try:
        bulb_escritorio.turn_off()
    except:
        ""
    try:
        bulb_quarto.turn_off()
    except:
        ""
    try:
        lampada_branca(bulb_corredor,2250,1)
    except:
        ""
    try:
        lampada_colorida(bulb_cozinha,235,95,75)
    except:
        ""
    #quinta_telhado_branco

#horaDoDino_yeelight()
#####################################################################


#Hora do Trabalho -- Done!
#####################################################################
def horaDoTrabalho_yeelight():
    try:
        lampada_branca(bulb_escritorio,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_sala_teto,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_sala_luminaria,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_sala_teto,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_cozinha,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_sala_teto,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_quarto,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_sala_teto,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_corredor,5000,100)
    except:
        ""
    try:
        lampada_branca(bulb_sala_teto,5000,100)
    except:
        ""

#horaDoTrabalho_yeelight()
#####################################################################


#Boa Noite -- Done!
#####################################################################
def boaNoite_yeelight():
    try:
        bulb_quarto.turn_off()
    except:
        ""
    try:
        bulb_sala_luminaria.turn_off()
    except:
        ""
    try:
        bulb_sala_teto.turn_off()
    except:
        ""
    try:
        bulb_escritorio.turn_off()
    except:
        ""
    try:
        lampada_branca(bulb_cozinha,1700,1)
    except:
        ""
    try:
        lampada_branca(bulb_corredor,1700,1)
    except:
        ""

#boaNoite_yeelight()
#####################################################################


#Arthur Dormir -- Done!
#####################################################################
def arthurDormir_yeelight():
    try:
        bulb_quarto.turn_off()
    except:
        ""
    try:
        bulb_escritorio.turn_off()
    except:
        ""
    try:
        lampada_branca(bulb_corredor,1700,1)
    except:
        ""

#arthurDormir_yeelight()
#####################################################################


#Escritório Hora do Trabalho -- Done!
#####################################################################
def trabalhoEscritorio_yeelight():
    try:
        bulb_escritorio.turn_on()
    except:
        ""
    try:
        lampada_branca(bulb_escritorio,5000,100)
    except:
        ""

#trabalhoEscritorio_yeelight()
#####################################################################