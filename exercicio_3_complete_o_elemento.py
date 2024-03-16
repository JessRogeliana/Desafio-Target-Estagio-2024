'''
Enunciado:
3) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
'''   


# a) 1, 3, 5, 7, ? 

i = 0
lista = []

while i < 10:
    if i % 2 != 0:
        lista.append(i)
    i += 1
print(lista) 

#Resultado: [1, 3, 5, 7, 9]




# b) 2, 4, 8, 16, 32, 64, ?

lista = []
valor = 2
while len(lista) < 7:
    if len(lista) == 0:
        lista.append(valor)
    else:
        valor += valor
        lista.append(valor)
print(lista) 

#Resultado: [2, 4, 8, 16, 32, 64, 128]




# c) 0, 1, 4, 9, 16, 25, 36, ?

lista = []
valor = 0
i = 1
while len(lista) < 8:
    lista.append(valor)
    valor += i
    i += 2
print(lista) 

#Resultado: [0, 1, 4, 9, 16, 25, 36, 49]




# d) 4, 16, 36, 64, ?

lista = []
valor = 2
while len(lista) < 5:
    lista.append(valor**2)
    valor += 2

print(lista)

#Resultado: [4, 16, 36, 64, 100]




# e) 1, 1, 2, 3, 5, 8, ?

numeros = [1, 1]
lista = []
while len(numeros) < 7:
    lista = numeros[-1] + numeros[-2]
    numeros.append(lista)

print(lista)

#Resultado: [1, 1, 2, 3, 5, 8, 13]




# f) 2, 10, 12, 16, 17, 18, 19, ?

print('200. A lógica está em todos os números que escritos em extenso comecem com a letra "D".')

#Resultado: 200.