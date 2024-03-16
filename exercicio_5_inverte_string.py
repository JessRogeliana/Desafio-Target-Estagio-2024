'''
Enunciado:
5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''


string = input('Digite uma palavra: ')
i = 1
saida = ''

while i <= len(string):
    saida += string[-i]
    i += 1

print(saida)

#Resultado: "etset" caso string = teste, por exemplo
