# -*- coding: utf-8 -*-
from selenium import webdriver
from openpyxl import load_workbook

import os
import sys
import time

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


def start_gerador():
    while True:
        chrome = None

        # VERIFICA SE A BASE DE DADOS EXISTE
        # base
        if os.path.isfile("base/BaseDeDados.xlsx"):
            wb = load_workbook(filename='base/BaseDeDados.xlsx')
            wb_ativo = wb.active
        else:
            print("Base de dados não encontrada!")
            sys.exit()

        # arquivos de texto
        if not os.path.isdir("base/noticias"):
            os.makedirs("base/noticias")
        else:
            pass

        print("Notícias na base: " + str(len(wb_ativo['B'])))

        try:
            # ABRE AS NOTICIAS DA BASE NO NAVEGADOR
            chrome = webdriver.Chrome(executable_path=str(os.path.abspath(os.curdir)) + r"\chromedriver.exe",
                                      options=options)

            noticias_base = wb_ativo['B']
            contador_noticias = 0
            for noticia in noticias_base:

                if os.path.isfile('base/noticias/noticia' + str(contador_noticias + 1) + ".txt"):
                    print('O arquivo noticia' + str(contador_noticias + 1) + ".txt já se encontra na base de notícias!")
                    contador_noticias += 1
                else:
                    # CHECA SE A NOTÍCIA É UM VÍDEO
                    if wb_ativo['C' + str(contador_noticias + 1)].value == "video":
                        print("\nA notícia " + str(contador_noticias + 1)
                              + " é um vídeo!\nPulando para a próxima...\n\n")
                        contador_noticias += 1
                    elif wb_ativo['C' + str(contador_noticias + 1)].value == "erro":
                        print("\nNotícia " + str(contador_noticias + 1) + " com erro!\nPulando para a próxima...\n\n")
                        contador_noticias += 1
                    else:
                        try:
                            chrome.get(noticia.value)

                            time.sleep(2)

                            # GERA ARQUIVO
                            titulo = chrome.find_element_by_xpath(".//h1[contains(@class, 'content-head')]").text
                            corpo = chrome.find_element_by_xpath(".//div[contains(@class, 'article-body')]").text

                            texto = corpo.splitlines()
                            txt = open("base/noticias/noticia" + str(contador_noticias + 1) + ".txt", "w")
                            txt.write(titulo + "\n\n")
                            for linha in texto:
                                txt.write(linha)
                                txt.write("\n")
                            txt.close()

                            print('O arquivo noticia' + str(contador_noticias + 1)
                                  + ".txt foi inserido na base de notícias.")

                            contador_noticias += 1
                        except Exception as e:
                            # CHECA SE A NOTÍCIA É UM VÍDEO
                            if "globoplay.globo.com/v/" in chrome.current_url:
                                print("\nA notícia " + str(contador_noticias + 1)
                                      + " é um vídeo.\nPulando para a próxima...\n\n")
                                wb_ativo['C' + str(contador_noticias + 1)] = "video"
                                wb.save(filename='base/BaseDeDados.xlsx')
                                contador_noticias += 1
                            else:
                                print("\nA notícia " + str(contador_noticias + 1)
                                      + " está com erro.\nPulando para a próxima...\n\n")
                                wb_ativo['C' + str(contador_noticias + 1)] = "video"
                                wb.save(filename='base/BaseDeDados.xlsx')
                                contador_noticias += 1
        except Exception as e:
            print(e)
            chrome.quit()

        chrome.quit()
        sys.exit()
