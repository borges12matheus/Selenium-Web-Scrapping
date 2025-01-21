from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from bs4 import BeautifulSoup
import requests
import pandas as pd

#NAVEGAÇÃO WEB
#Instalando o webdriver
servico = Service(ChromeDriverManager().install())

#Criando o navegador GoogleChrome
navegador = webdriver.Chrome(service= servico)
CSS_SELECTOR = "css selector"

#Acessando o link desejado
link = "https://www.google.com/travel/flights/"
navegador.get(link)

#INPUTS DE PESQUISA DAS PASSAGENS
origem = "Uberlândia"
destino = "Recife"
data_ida = date.today().day
data_volta = 20

#NAVEGANDO NO SITE COM BASE NOS INPUTS
navegador.find_element('xpath', '//*/div[1]/div/div/div[1]/div/div/input').click()
time.sleep(2)
navegador.find_element('xpath', '//*/div[6]/div[2]/div[2]/div[1]/div/input').clear()
navegador.find_element('xpath', '//*/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(origem)
navegador.find_element('xpath', '//*/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)
navegador.find_element('xpath', '//*/div[4]/div/div/div[1]/div/div/input').click()
time.sleep(2)
navegador.find_element('xpath', '//*/div[6]/div[2]/div[2]/div[1]/div/input').clear()
navegador.find_element('xpath', '//*/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(destino)
navegador.find_element('xpath', '//*/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)

navegador.find_element('xpath','//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input').click()
time.sleep(2)
navegador.find_element('xpath','//*/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input').clear()
navegador.find_element('xpath','//*/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input').send_keys(data_ida)
navegador.find_element('xpath','//*/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input').send_keys(Keys.ENTER)

navegador.find_element('xpath','//*/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').clear()
navegador.find_element('xpath','//*/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').send_keys(data_volta)
navegador.find_element('xpath','//*/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').send_keys(Keys.ENTER)

navegador.find_element('xpath','//*/div[2]/div/div[3]/div[3]/div/button').click()
time.sleep(2)
navegador.find_element('xpath','//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button').click()

#Filtro para passagem ida e volta/ida
time.sleep(2)
botao_tipoVoo = navegador.find_element('xpath', '//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[1]/div')
botao_classeVoo = navegador.find_element('xpath', '//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div[1]')


#--------------------------WEB SCRAPING------------------------------------------
#Cria função de filtragem da página
def filtroVoos(tipo_filtro):
          
    if tipo_filtro == 0:
   #FILTRO DAS PASSSAGENS IDA E VOLTA
        #Selecionando a classe econômica premium
        time.sleep(1)
        botao_classeVoo.click()
        time.sleep(1)
        botao_classeVoo.find_element('xpath', '//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[2]').click()
        tipo_filtro = 1
        tipo_classe = 'economica_premium'
        return(tipo_filtro,tipo_classe)
        
    if tipo_filtro == 1:
    #Selecionando a classe executiva
        time.sleep(1)
        botao_classeVoo.click()
        time.sleep(1)
        botao_classeVoo.find_element('xpath','//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[3]').click()
        tipo_filtro = 2
        tipo_classe = 'executiva'
        return(tipo_filtro,tipo_classe)
        
    if tipo_filtro == 2:
    #Selecionando a primeira classe
        time.sleep(1)
        botao_classeVoo.click()
        time.sleep(1)
        botao_classeVoo.find_element('xpath','//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[4]').click()
        tipo_filtro = 3
        tipo_classe = 'primeira'
        return(tipo_filtro,tipo_classe)
    
    #FILTRO DAS PASSSAGENS SOMENTE DE IDA
    if tipo_filtro == 3:
        #Selecionando só ida e classe econômica
        time.sleep(1)
        botao_tipoVoo.click()
        time.sleep(1)
        botao_tipoVoo.find_element('xpath', '//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]').click()
        time.sleep(1)
        botao_classeVoo.click()
        botao_classeVoo.find_element('xpath','//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[1]').click()
        tipo_filtro = 4
        tipo_classe = 'economica'
        return(tipo_filtro,tipo_classe)
        
    if tipo_filtro == 4:
    #Selecionando a classe econômica premium
        time.sleep(1)
        botao_classeVoo.click()
        time.sleep(1)
        botao_classeVoo.find_element('xpath', '//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[2]').click()
        tipo_filtro = 5
        tipo_classe = 'economica_premium'
        return(tipo_filtro,tipo_classe)
        
    if tipo_filtro == 5:
    #Selecionando a classe executiva
        time.sleep(1)
        botao_classeVoo.click()
        time.sleep(1)
        botao_classeVoo.find_element('xpath','//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[3]').click()
        tipo_filtro = 6
        tipo_classe = 'executiva'
        return(tipo_filtro,tipo_classe)
        
    if tipo_filtro == 6:
    #Selecionando a primeira classe
        time.sleep(1)
        botao_classeVoo.click()
        time.sleep(1)
        botao_classeVoo.find_element('xpath','//*/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[4]').click()
        tipo_filtro = 7
        tipo_classe = 'primeira'
        return(tipo_filtro,tipo_classe)

# page_content = navegador.page_source
# page = BeautifulSoup(page_content, 'html.parser')
dados_passagem = []
tipo_filtro = 0
tipo_classe = 'economica'

for i in range(8):  
    time.sleep(2)
    page_content = navegador.page_source
    page = BeautifulSoup(page_content, 'html.parser')
    tag_voos = page.find_all('li', class_ = 'pIav2d')
    print('-------'+tipo_classe+'-------')
    for tag_voo in tag_voos:
        
        #Horário Voo
        horario = tag_voo.find_all('span',attrs= {'jscontroller':'cNtv4b'})
        horario = horario[0].get_text()+' - '+horario[1].get_text()
        print(horario)
        
        #Companhia Áerea
        empresa = tag_voo.find('div', class_ = 'sSHqwe tPgKwe ogfYpf').find('span').text
        print(empresa)
        
        #Duração do voo
        duracao = tag_voo.find('div', class_ = 'gvkrdb AdWm1c tPgKwe ogfYpf').text
        print(duracao)
        
        #Aeroporto
        tag_aeroporto = tag_voo.find('div', attrs= {'class':'Ak5kof'})
        aeroporto = tag_aeroporto.find_all('span',attrs= {'jscontroller':'cNtv4b'})
        aeroporto_ida = aeroporto[0].get_text()
        aeroporto_chegada = aeroporto[1].get_text()
        print(aeroporto_ida, aeroporto_chegada)
        
        #Escala de voo
        tag_escala = tag_voo.find('div',class_= 'BbR8Ec')
        n_escala = tag_escala.find('span', class_= 'ogfYpf').text
        info_escala = tag_escala.find('div', class_= 'sSHqwe tPgKwe ogfYpf').get_text("-", strip= True)
        print(n_escala+ ' - ' + info_escala)
        
        #Preço do Voo
        tag_preco = tag_voo.find('div', class_= 'U3gSDe')
        preco = tag_preco.find('div', class_= 'BVAVmf I11szd POX3ye').text
        tipo_passagem = tag_preco.find('div', class_= 'N872Rd sSHqwe I11szd POX3ye').text
        print(preco +' - '+ tipo_passagem)
        print('---------------------------')
        if tipo_passagem == '':
            tipo_passagem = 'ida'
        dados_passagem.append([horario, empresa, duracao, aeroporto_ida, aeroporto_chegada,
                               n_escala, info_escala, preco, tipo_passagem,tipo_classe])
        
        #print(page.prettify())
    if i<7:
        tipo_classe = filtroVoos(i)[1]

#navegador.close()
dados= pd.DataFrame(dados_passagem, columns=['horario_voo', 'companhia_aerea', 'duracao',
                                            'aeroporto_saida', 'aeroporto_chegada','escalas',
                                            'informacoes_escala', 'preco' , 'tipo_passagem','tipo_classe'])
dados.to_excel(origem+'-'+destino+'.xlsx', index= False)
