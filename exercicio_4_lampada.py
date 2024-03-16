'''
Enunciado:
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
'''

inter1 = False
inter2 = False
inter3 = False

lamp1 = False
lamp2 = True
lamp3 = False

aspecto = 'quente'

resultado = {}

# Ligar o primeiro interruptor e aguarde um pouco. 
print("Ligando o primeiro interruptor...")
inter1 = True

# Desligar o primeiro interruptor e ligar o segundo. 
print("Ligando o segundo interruptor...")
inter1 = False
inter2 = True

# Ir até a sala e verificar as lampadas

if lamp1 == False and aspecto == "quente":
    print("A lampada 1 corresponde ao interruptor 1")
    resultado["lampada 1"] = "interruptor 1"

    if lamp2:
        print("A lampada 2 corresponde ao interruptor 2")
        new = {'lampada 2' : 'interruptor 2'}
        resultado.update(new)

        print("A lampada 3 corresponde ao interruptor 3")
        new = {'lampada 3' : 'interruptor 3'}
        resultado.update(new)
    
    else: #lamp2 == False
        print("A lampada 2 corresponde ao interruptor 3")
        new = {'lampada 2' : 'interruptor 3'}
        resultado.update(new)
    
        print("A lampada 3 corresponde ao interruptor 2")
        new = {'lampada 3' : 'interruptor 2'}
        resultado.update(new)

elif lamp1:
    print("A lampada 1 corresponde ao interruptor 2")
    resultado["lampada 1"] = "interruptor 2"

    if lamp2 == False and aspecto == "quente":
        print("A lampada 2 corresponde ao interruptor 1")
        new = {'lampada 2' : 'interruptor 1'}
        resultado.update(new)

        print("A lampada 3 corresponde ao interruptor 3")
        new = {'lampada 3' : 'interruptor 3'}
        resultado.update(new)

    else: #lamp2 == False
        print("A lampada 2 corresponde ao interruptor 3")
        new = {'lampada 2' : 'interruptor 3'}
        resultado.update(new)
    
        print("A lampada 3 corresponde ao interruptor 1")
        new = {'lampada 3' : 'interruptor 1'}
        resultado.update(new)

else:
    print("A lampada 1 corresponde ao interruptor 3")
    resultado["lampada 1"] = "interruptor 3"

    if lamp2 == False and aspecto == "quente":
        print("A lampada 2 corresponde ao interruptor 1")
        new = {'lampada 2' : 'interruptor 1'}
        resultado.update(new)

        print("A lampada 3 corresponde ao interruptor 2")
        new = {'lampada 3' : 'interruptor 2'}
        resultado.update(new)

    else: #lamp2 == True 
        print("A lampada 2 corresponde ao interruptor 2")
        new = {'lampada 2' : 'interruptor 2'}
        resultado.update(new)

        print("A lampada 3 corresponde ao interruptor 1")
        new = {'lampada 3' : 'interruptor 1'}
        resultado.update(new)

print(resultado)

# Resultado: {'lampada 1': 'interruptor 1', 'lampada 2': 'interruptor 2', 'lampada 3': 'interruptor 3'}