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

url_base = "https://www.reclameaqui.com.br/empresa/c6-bank/lista-reclamacoes/?busca=pix&pagina="

option = Options()
option.headless = False
driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
driver.get(url=url_base)

div_reclamacoes = driver.find_element(By.CLASS_NAME, "eFXbXn")

cont_html = div_reclamacoes.get_attribute('outerHTML')
sopa = BeautifulSoup(cont_html, 'html.parser')

lista_reclamacao = sopa.find_all('div', class_ = 'bJdtis')

# print(lista_reclamacao)

titulos = []
textos = []

for reclamacao in lista_reclamacao:
    titulo = reclamacao.select('a h4')
    texto = reclamacao.select('p')
    titulos.append(titulo[0].get_text())
    textos.append(texto[0].get_text())
    print(titulo[0].get_text())
    print('~X------------V----------X~')
    print(texto[0].get_text())
    print('~X------------^----------X~')

print('AQ:')

titulosUnicos = []

for titulo in titulos:
    tituloStr = str(titulo)
    palavra = tituloStr.split()
    for palavra2 in palavra:
        titulosUnicos.append(palavra2)

titulosFiltrados = []

print(titulosUnicos)


# print("AAA" + type(texto))

# print(sopa.prettify())

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(url_base + '\chromedriver.exe', options = chrome_options)

# # driver.get(url = "https://www.reclameaqui.com.br/empresa/c6-bank/lista-reclamacoes/?busca=pix&pagina", self=driver.get)

# # reclamacoes = []
# # tituloReclamacao = []
# # link = []
