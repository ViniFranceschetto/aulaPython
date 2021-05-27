import random

minuscula = "abcdefghijklmnopqrstuvwxyz"
maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "{}[]()*#@$;./,_-"

all = minuscula+maiuscula+numeros+simbolos
tamanho = int(input("digite tamanho da senha: "))

password = "".join(random.sample(all, tamanho))
print(password)
