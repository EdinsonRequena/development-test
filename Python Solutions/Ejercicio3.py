import random
array = [int(random.random()*11),int(random.random()*11),int(random.random()*11),int(random.random()*11),int(random.random()*11)]
print("Entrada: "+str(array))
i = 0
def sumarElementos(elementos):
    for i in range(1,len(elementos)):
        if i>0:
            elementos[i]+=elementos[(i-1)]
    print("Salida: "+str(elementos))

sumarElementos(array)