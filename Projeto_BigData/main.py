# -*- coding: utf-8 -*-
# IMPORTS

import scrape
import gerador
import analise
import sys
import os


def main(argumentos):
    if len(argumentos) == 2:
        arg1 = argumentos[1]

        if str(arg1).lower() == "menu":
            print("╔══════════════════════════════════════════════════════════════════════════════╗")
            print("║                    Projeto de Análise de Dados e Big Data                    ║")
            print("╠══════════════════════════════════════════════════════════════════════════════╣")
            print("║                                                                              ║")
            print("║    Para inicializar selecione um dos programas abaixo para ser executado:    ║")
            print("║                                                                              ║")
            print("║                                                                              ║")
            print("║         scrape  » Robô de coleta de dados de páginas web                     ║")
            print("║                                                                              ║")
            print("║         gerador » Robô que gera os arquivos para análise                     ║")
            print("║                                                                              ║")
            print("║         analise » Robô que faz a análise do conteúdo das matérias            ║")
            print("║                   coletadas pelo robô de scrape                              ║")
            print("║                                                                              ║")
            print("║                                                                              ║")
            print("║        Para começar, utilize o seguinte comando:                             ║")
            print("║                                                                              ║")
            print("║        ┌────────────────────────────────────────────────────────────┐        ║")
            print("║        │ python main.py [NOME DO PROGRAMA]                          │        ║")
            print("║        └────────────────────────────────────────────────────────────┘        ║")
            print("║                                                                              ║")
            print("╚══════════════════════════════════════════════════════════════════════════════╝")
        elif str(arg1).lower() == "scrape":
            print("Inicializando robô de coleta de dados...\n")
            scrape.start_scrape()
        elif str(arg1).lower() == "gerador":
            print("Inicializando robô de geração de dados...\n")
            gerador.start_gerador()
        elif str(arg1).lower() == "analise" or str(arg1).lower() == "análise":
            print("Inicializando robô de análise...")
            analise.start_analise()
        else:
            print("Digite um argumento válido!")
    else:
        print("Digite um argumento válido!")


if __name__ == "__main__":
    main(sys.argv)
