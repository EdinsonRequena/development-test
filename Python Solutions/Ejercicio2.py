import random
cadena = []
i = 0
def convertirAString(numero):
    print("Numero limite: "+str(numero))
    for i in range(1,numero):
        salida =""
        if i%3==0:
            salida+= "Plic"
        if i%5==0:
            salida+= "Plac"
        if i%7==0:
            salida+= "Ploc"
        if salida=="":
            salida=str(i)
        print(salida)

valor = int(random.random() * 1001)
convertirAString(valor)