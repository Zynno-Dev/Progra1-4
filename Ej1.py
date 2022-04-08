import random
import math

lista = [(random.randint(0,100)) for i in range(99)]
print(lista)

listaPares = [ i for i in lista if i%2==0]
print(listaPares)

listaImpares = [ i for i in lista if i%2!=0]
print(listaImpares)

listaCalculator = [math.sin(i) if i%2==0 else math.cos(i) for i in lista]
print("calc")
print(listaCalculator)
