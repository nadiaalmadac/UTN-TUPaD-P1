#Ejercicio 1
lista=list(range(4,101,4))
print(lista)
#Ejercicio 2
lista=[7,18,19,24,66]
print(lista[-2])
#Ejercicio 3
lista=[]
lista.append("hola")
lista.append("como")
lista.append("vas")
print(lista)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[-1]="oso"
print(animales)

#Ejercicio 5
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
#Lo que hace es identificar cual es el máximo de los valores con la función max(…) y borrarlo con remove

#Ejercicio 6
lista=list(range(10,31,5))
print(lista[0],lista[1])


#Ejercicio 7
autos=["sedan", "polo", "suran", "gol"]
autos[1]="jeep"
autos[2]="palio"
print(autos)

#Ejercicio 8
dobles=[]
for i in range(5,16,5):
    dobles.append(2*i)
print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
print(compras)

#Ejercicio 10
lista_anidada=[]
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([])
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada.append(False)
print(lista_anidada)