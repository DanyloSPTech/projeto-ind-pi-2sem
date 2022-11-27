# Web Scraping do Site do Reclame Aqui | Danylo Dias Gomes
# Bibliotecas Utilizadas: selenium & bs4
# python -m pip install selenium
# python -m pip install bs4
# python -m pip install webdriver_manager

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from os import path
from os import getcwd
import csv
from palavras_chave import palavras_chave
import platform
import subprocess

so = platform.system()

user_agente = ''

if so == 'Windows':
    user_agente = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
elif so == 'Linux':
    user_agente = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"


option = Options()
option.add_argument("--headless")
option.add_argument(f"user-agent={user_agente}")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)

i = 1

titulos = []
textos = []

while i <= 25:
    url_base = f"https://www.reclameaqui.com.br/empresa/c6-bank/lista-reclamacoes/?busca=pix&pagina={i}"
    driver.get(url=url_base)
    
    driver.get_screenshot_as_file("screenshot.png")
    
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
            for x in palavras_chave:
                if palavra == x:
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
            for x in palavras_chave:
                if palavra == x:
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
                        
    print("Titulos: \n")
    for palavra in titulos:
        print(palavra + '\n')
    print("\n\nTextos:\n")
    for palavra in textos:
        print(palavra + '\n')
        
        
    i += 1
    
driver.close()

# Chamando script em R responsável por gerar a wordcloud
subprocess.call(['Rscript', 'E:/Users/Danyl/Documents/GitHub/projeto-ind-pi-2sem/caca-reclamacao/wordcloud/script_word_cloud.r'])