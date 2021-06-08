# -*- coding: utf-8 -*-
import os
import sys
import shutil


def start_analise():
    if os.path.isdir("base/noticias"):
        if len(os.listdir('base/noticias')) > 0:
            print(str(len(os.listdir('base/noticias'))) + " Notícia(s) encontrada(s)!")
            print("Começando análise!\n\n")
    else:
        print("Base de dados não encontrada!")
        sys.exit()

    # CRIACAO DOS DIRETORIOS
    if not os.path.isdir("base/noticias_4"):
        os.makedirs("base/noticias_4")
    else:
        pass

    if not os.path.isdir("base/noticias_6"):
        os.makedirs("base/noticias_6")
    else:
        pass

    if not os.path.isdir("base/noticias_8"):
        os.makedirs("base/noticias_8")
    else:
        pass

    # TERMOS PARA PESQUISA
    palavras_chave = ['covid', 'teste', 'testes', 'testam', 'testaram', 'testou', 'positivo', 'negativo', 'casos',
                      'mais de', 'pandemia', 'quarentena', 'internado', 'entubado', 'uti', 'morre', 'morrem',
                      'complicações', 'suspenso', 'suspensa', 'suspensos', 'suspensas', 'afastado', 'afastada',
                      'afastados', 'afastadas']

    # LEITURA DOS ARQUIVOS
    noticias_com_erro = []
    noticias_analisadas = []
    noticias_8 = []
    noticias_6 = []
    noticias_4 = []
    numero_noticias = len(os.listdir('base/noticias'))
    contador_analise = 0
    while contador_analise < numero_noticias:
        try:
            noticia = open("base/noticias/noticia" + str(contador_analise + 1) + ".txt", "r").read()

            # ANALISE DO CONTEUDO DO ARQUIVO
            termos = []
            contador_termos = 0
            for palavra_chave in palavras_chave:
                if palavra_chave in noticia.lower():
                    termos.append(palavra_chave)
                    contador_termos += 1

            # GUARDA NOTICIAS COM 4 OU MENOS TERMOS
            if 0 < contador_termos <= 4:
                noticias_4.append(str(contador_analise + 1))
                if not os.path.isfile("base/noticias_4/noticia" + str(contador_analise + 1) + ".txt"):
                    shutil.move("base/noticias/noticia" + str(contador_analise + 1) + ".txt",
                                "base/noticias_4/noticia" + str(contador_analise + 1) + ".txt")
                else:
                    pass

            # GUARDA NOTICIAS QUE TENHAM ENTRE 4 E 6 TERMOS
            elif 4 < contador_termos <= 6:
                noticias_6.append(str(contador_analise + 1))
                if not os.path.isfile("base/noticias_6/noticia" + str(contador_analise + 1) + ".txt"):
                    shutil.move("base/noticias/noticia" + str(contador_analise + 1) + ".txt",
                                "base/noticias_6/noticia" + str(contador_analise + 1) + ".txt")
                else:
                    pass

            # GUARDA NOTICIAS COM 8 TERMOS OU MAIS
            elif contador_termos >= 8:
                noticias_8.append(str(contador_analise + 1))
                if not os.path.isfile("base/noticias_8/noticia" + str(contador_analise + 1) + ".txt"):
                    shutil.move("base/noticias/noticia" + str(contador_analise + 1) + ".txt",
                                "base/noticias_8/noticia" + str(contador_analise + 1) + ".txt")
                else:
                    pass

            noticias_analisadas.append(str(contador_analise + 1))
            contador_analise += 1
        except:
            # GUARDA NOTICIAS COM ERRO DE LEITURA
            noticias_com_erro.append(str(contador_analise + 1))

            contador_analise += 1

    # MOSTRA RESULTADOS
    print(str(len(noticias_analisadas)) + " notícias analisadas")
    print(str(len(noticias_8)) + " notícias com 8 ou mais termos pesquisados")
    print(str(len(noticias_6)) + " notícias com 6 a 8 termos pesquisados")
    print(str(len(noticias_4)) + " notícias com até 4 termos pesquisados")
    print(str(len(noticias_com_erro)) + " notícias com erro")

    sys.exit()
