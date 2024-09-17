from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def obter_codigos():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)

    url = 'https://www.infomoney.com.br/ferramentas/altas-e-baixas/'

    driver.get(url)

    sleep(6)

    site = BeautifulSoup(driver.page_source, 'html.parser')

    linhas = site.find_all('tr', {'role':'row'})

    acoes = []

    for i in linhas[1:]:
        codigos = i.find("a")
        acoes.append(codigos.text)

    driver.quit()

    return acoes

def buscar_dados():

    return