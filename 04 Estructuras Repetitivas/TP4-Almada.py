#Ejercicio 1
for i in range(101):
    print(i);
#Ejercicio 2
flag=0
num_string="10"

cifras=1
n=int(input("Ingrese un número: "))
while(flag==0):
    num=int(num_string)
    if(int(n/num)==0):
          print(f"El número tiene {cifras} cifras");
          flag=1;
    else:
          cifras=cifras+1
          num_string=num_string+"0"
          print(cifras)
          print(n/num)
 #Ejercicio 3
 a=int(input("Ingrese el número entero inicial:"))
b=int(input("Ingrese el número entero final:"))
cont=0
for i in range(a+1,b,1):
    cont=cont+i
print(f"La suma de todos los números comprendidos entre {a} y {b} es {cont}")
#Ejercicio 4

print("El siguiente programa va a sumar todos los números que ingrese. Para poder salir debe ingresar 0.")
a=int(input("Ingrese número:"))
cont=0
while(a!=0):
   cont=a+cont
   a=int(input("Ingrese número:"))
print(f"La suma es: {cont}")

#Ejercicio 5
import random
numero_correcto=random.randint(0, 9)
flag=0
cont=0

while(flag==0):
    numero_del_usuario=int(input("Ingrese un número entre 0 y 9 para adivinar:"))
    if(numero_correcto==numero_del_usuario):
        flag=1
        print("Acertó el número")
    cont=cont+1
             
print(f"Ustede acertó en el intento número {cont}") 

#Ejercicio 6
for i in range(100,0,-2):
    print(i)

#Ejercicio 7
a=int(input("Ingrese un número positivo: "))
suma=0
if(a>0):
    for i in range(0,a+1,1):
        suma=i+suma
    print(f"La suma desde 0 a {a} es: {suma}")
else:print("Ingresó un número negativo o 0")

#Ejercicio 8
print("Usted debe ingresar 100 números enteros, con un enter podrá ingresar uno tras otro")
positivo=0
negativo=0
cero=0
pares=0
impares=0
for i in range (0,100,1):
    a=int(input())
    if (a>0):
        positivo=positivo+1
    elif(a<0):
        negativo=negativo+1
    else: cero=cero+1
    if (a%2==0):
        pares=pares+1
    else: impares=impares+1
print(f"Hay {impares} impares y {pares} pares")
print(f"Ingresó {negativo} negativos, {positivo} positivos y {cero} ceros")

#Ejercicio 9
print("Usted debe ingresar 100 números enteros, con un enter podrá ingresar uno tras otro")
suma=0
for i in range (0,100,1):
    n=int(input())
    suma=n+suma
media=suma/100
print(f"El promedio es: {media}")

#Ejercicio 10
a=input("Ingrese un número ")
numero_nuevo=""
fin=len(a)
for i in range (0,fin,1):
      n=len(a)
      ultimo_numero=a[n-1:n]
      a=a[0:n-1]
      numero_nuevo=numero_nuevo+ultimo_numero

print(f"El número invertido es :{numero_nuevo}")