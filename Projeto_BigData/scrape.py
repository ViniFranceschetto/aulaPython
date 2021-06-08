# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

import time
import sys
import os

options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--enable-images")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-certificate-errors-skpi-list")
options.add_argument("--ignore-ssl-errors")
options.add_argument("no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--test-type")
options.add_argument("--app-auto-launched")
options.add_argument("--enable-internal-media-session")
options.add_argument("--ignore-urlfetcher-cert-requests")
options.add_argument("--oobe-guest-session")
options.add_argument("--account-consistency")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


def start_scrape():
    chrome = webdriver.Chrome(executable_path=str(os.path.abspath(os.curdir)) + r"\chromedriver.exe", options=options)
    chrome.get("https://globoesporte.globo.com")

    time.sleep(3)

    # PESQUISA
    buscar = chrome.find_element_by_xpath(".//input[@id='busca-campo']")
    time.sleep(1)
    buscar.send_keys("jogadores com covid")
    time.sleep(1)
    buscar.send_keys(Keys.ENTER)

    time.sleep(5)

    # GERAÇÃO DO EXCEL
    if os.path.isfile("base/BaseDeDados.xlsx"):
        os.remove("base/BaseDeDados.xlsx")
    else:
        pass

    wb = Workbook()
    try:
        wb.remove(wb['Sheet'])
    except Exception as e:
        # print(str(e))
        pass
    wb.create_sheet("BaseDeDados")
    wbAtivo = wb.active

    # CAPTAÇÃO DE NOTÍCIAS
    lstNoticias = None
    contadorNoticia = 1
    pagina = 1
    while pagina < 5:
        url = ""
        noticias = ""

        if '&page=' in str(chrome.current_url):
            url = str(chrome.current_url).split("&page=")[0] + "&page=" + str(pagina)
        elif '&page=' not in str(chrome.current_url):
            url = str(chrome.current_url) + "&page=" + str(pagina)

        chrome.get(url)
        noticias = chrome.find_elements_by_xpath(".//a[.//*[contains(text(), 'Covid') or contains(text(), 'covid')]]")

        lstNoticias = []
        for noticia in noticias:
            print("---------------------- Notícia " + str(contadorNoticia) + " inserida! ----------------------\n"
                  + noticia.text
                  + "\nLink: " + noticia.get_attribute('href') + "\n\n")
            lstNoticias.append(noticia.get_attribute('href'))
            wbAtivo.append([contadorNoticia, noticia.get_attribute('href')])

            contadorNoticia += 1

        time.sleep(1.5)
        pagina += 1

    # CRIA PASTA DA BASE DE DADOS
    if not os.path.exists("base"):
        os.makedirs("base")
    else:
        pass

    # SALVA BASE DE DADOS
    wb.save(filename='base/BaseDeDados.xlsx')

    wb.close()

    chrome.quit()
    sys.exit()
