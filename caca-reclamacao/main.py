# Web Scraping do Site do Reclame Aqui | Danylo Dias Gomes
# Bibliotecas Utilizadas: selenium & bs4
# python -m pip install selenium
# python -m pip install bs4

from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

url_base = "https://www.reclameaqui.com.br/empresa/c6-bank/"