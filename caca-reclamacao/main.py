# Web Scraping do Site do Reclame Aqui | Danylo Dias Gomes
# Bibliotecas Utilizadas: selenium & bs4
# python -m pip install selenium
# python -m pip install bs4
# python -m pip install webdriver_manager

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
from os import path
from os import getcwd
import csv

url_base = "https://www.reclameaqui.com.br/empresa/c6-bank/lista-reclamacoes/?busca=pix&pagina="

option = Options()
option.headless = False
driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
driver.get(url=url_base)

i = 1

titulos = []
textos = []

while i <= 25:
    url_base = f"https://www.reclameaqui.com.br/empresa/c6-bank/lista-reclamacoes/?busca=pix&pagina={i}"
    driver.get(url=url_base)
    
    div_reclamacoes = driver.find_element(By.CLASS_NAME, "eFXbXn")

    cont_html = div_reclamacoes.get_attribute('outerHTML')
    sopa = BeautifulSoup(cont_html, 'html.parser')

    lista_reclamacao = sopa.find_all('div', class_ = 'bJdtis')

    # print(lista_reclamacao)

    for reclamacao in lista_reclamacao:
        titulo = reclamacao.select('a h4')
        texto = reclamacao.select('p')
        
        titulosUnicos = []
        textosUnicos = []
        
        tituloStr = str(titulo[0].get_text())
        palavrasTi = tituloStr.split()
        for palavra in palavrasTi:
            palavraTratada = palavra.lower()
            print(palavraTratada + '\n-------------')
            titulosUnicos.append(palavraTratada)

        textoStr = str(texto[0].get_text())
        palavrasTe = textoStr.split()
        for palavra in palavrasTe:
            palavraTratada = palavra.lower()
            print(palavraTratada + '\n-------------')
            textosUnicos.append(palavraTratada)
            
        for palavra in titulosUnicos:
            if(
                palavra == "lentidão" or 
                palavra == "lento" or 
                palavra == "travamento" or 
                palavra == "travou" or
                palavra == "bloqueio" or
                palavra == "bloqueado" or
                palavra == "caiu" or
                palavra == "caindo" or
                palavra == "transferência" or
                palavra == "pagamento" or
                palavra == "falha" or
                palavra == "falhou" or
                palavra == "app" or
                palavra == "aplicativo" or
                palavra == "demora" or
                palavra == "zerado" or
                palavra == "token" or
                palavra == "validação" or
                palavra == "qrcode" or
                palavra == "scanner" or
                palavra == "camera" or
                palavra == "sumir" or
                palavra == "sumir" or
                palavra == "cancelado" or
                palavra == "cancelamento" or
                palavra == "cancelar" or
                palavra == "receber" or
                palavra == "extorno" or
                palavra == "extornar"
            ):
                titulos.append(palavra)
                
                caminho = getcwd()
                
                if path.isfile(f'{caminho}\words_scraper.csv'):
                    with open('words_scraper.csv', 'a', newline='', encoding='UTF8') as arquivo:
                        writer = csv.DictWriter(arquivo, fieldnames=['Palavra'])
                        writer.writerow({'Palavra': palavra})
                else:
                    with open('words_scraper.csv', 'w', newline='', encoding='UTF8') as arquivo:
                        writer = csv.DictWriter(arquivo, fieldnames=['Palavra'])
                        writer.writeheader()
                        writer.writerow({'Palavra': palavra})
                
        for palavra in textosUnicos:
            if(
                palavra == "lentidão" or 
                palavra == "lento" or 
                palavra == "travamento" or 
                palavra == "travou" or
                palavra == "bloqueio" or
                palavra == "bloqueado" or
                palavra == "caiu" or
                palavra == "caindo" or
                palavra == "transferência" or
                palavra == "pagamento" or
                palavra == "falha" or
                palavra == "falhou" or
                palavra == "app" or
                palavra == "aplicativo" or
                palavra == "demora" or
                palavra == "zerado" or
                palavra == "token" or
                palavra == "validação" or
                palavra == "qrcode" or
                palavra == "scanner" or
                palavra == "camera" or
                palavra == "sumir" or
                palavra == "sumir" or
                palavra == "cancelado" or
                palavra == "cancelamento" or
                palavra == "cancelar" or
                palavra == "receber" or
                palavra == "extorno" or
                palavra == "extornar"
            ):
                textos.append(palavra)
                
                caminho = getcwd()
                
                if path.isfile(f'{caminho}\words_scraper.csv'):
                    with open('words_scraper.csv', 'a', newline='', encoding='UTF8') as arquivo:
                        writer = csv.DictWriter(arquivo, fieldnames=['Palavra'])
                        writer.writerow({'Palavra': palavra})
                else:
                    with open('words_scraper.csv', 'w', newline='', encoding='UTF8') as arquivo:
                        writer = csv.DictWriter(arquivo, fieldnames=['Palavra'])
                        writer.writeheader()
                        writer.writerow({'Palavra': palavra})
                        
        
        
        # print(titulo[0].get_text())
        # print('~X------------V----------X~')
        # print(texto[0].get_text())
        # print('~X------------^----------X~')
    print("Titulos: \n")
    for palavra in titulos:
        print(palavra + '\n')
    print("\n\nTextos:\n")
    for palavra in textos:
        print(palavra + '\n')
        
        
    i += 1

# print("AAA" + type(texto))

# print(sopa.prettify())

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(url_base + '\chromedriver.exe', options = chrome_options)

# # driver.get(url = "https://www.reclameaqui.com.br/empresa/c6-bank/lista-reclamacoes/?busca=pix&pagina", self=driver.get)

# # reclamacoes = []
# # tituloReclamacao = []
# # link = []
