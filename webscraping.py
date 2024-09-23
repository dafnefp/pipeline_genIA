import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


def obter_codigos():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver = webdriver.Chrome(options=options)

        url = 'https://www.infomoney.com.br/ferramentas/altas-e-baixas/'

        driver.get(url)

        site = BeautifulSoup(driver.page_source, 'html.parser')

        linhas = site.find_all('tr', {'role':'row'})

        acoes = []

        for i in linhas[1:]:
            codigos = i.find("a")
            acoes.append(codigos.text)

        sleep(2)

        driver.quit()

        return acoes

    except Exception as e:
        driver.quit()
        raise e


def buscar_dados(escolha, datamin, datamax):

    """
    Webscraping para buscar informações sobre uma determinada ação em um período especifico.

    Args:
        escolha (Str): código da ação
        datamin (date): data inicial do período das informações
        datamax (date): data final do período das informações
    """
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver = webdriver.Chrome(options=options)

        url_acao = f'https://www.infomoney.com.br/{escolha}'
        driver.get(url_acao)

        botao = driver.find_element(By.XPATH, "//a[span[text()='Histórico']]")
        botao.click()

        sleep(2)

        data_min = driver.find_element(By.ID, 'dateMin')
        data_max = driver.find_element(By.ID, 'dateMax')

        data_min.send_keys(datamin.strftime("%d/%m/%Y"))
        data_max.send_keys(datamax.strftime("%d/%m/%Y"))

        filtro = driver.find_element(By.ID, 'see_all_quotes_history')
        filtro.click()

        sleep(2)

        table = driver.find_element(By.ID, 'quotes_history')

        rows = table.find_elements(By.TAG_NAME, 'tr')

        cabecalho = rows[0].find_elements(By.TAG_NAME, 'th')

        titulo = []

        for texto in cabecalho:
            titulo.append(texto.text)

        df = pd.DataFrame(columns=titulo)

        for row in rows[1:]:
            # Find all the cells in the row
            cells = row.find_elements(By.TAG_NAME, 'td')

            # Extract text from each cell
            row_data = [cell.text for cell in cells]

            df.loc[len(df)] = row_data

        driver.quit()

        return df
    
    except Exception as e:
        driver.quit()
        raise e