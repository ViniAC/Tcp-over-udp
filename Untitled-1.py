from random import randint

fila = []
loop = ("SIM")
tamFila = None
tempoTotal = None
novaFila = None
#calcular tempo de atendimento-- numero de clientes e cada cliente num tempo aleatorio
def calcTempo():
    tempoTotal = 0
    for x in range(1, len(fila)):
        tempoTotal = tempoTotal + 3
    return tempoTotal

#confFila define o tamanho da fila e limpa a fila anterior
def confFila(tamFila, fila):
    tamFila = None
    tamFila = randint(1, 50)
    fila = []
    return tamFila, fila

#loop da fila
while loop == ("SIM"):
    loop = input("Você deseja atender o lote?\n Responda com SIM ou NAO\n")
    tamFila = None
    tamFila, fila = confFila(tamFila, fila)
    while (len(fila) <= tamFila):
        fila.append(1)
    tempoTotal = calcTempo()
    print("A fila ", fila, "foi atendida em ", tempoTotal, "segundos.")