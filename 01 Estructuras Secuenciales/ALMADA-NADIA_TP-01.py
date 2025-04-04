import math
#ejercicio 1
print("Ejercicio 1")
print("Hola mundo")
#ejercicio 2
print("Ejercicio 2")
a=input("Ingrese su nombre:")
print(f"Hola {a}!")
#ejercicio 3
print("Ejercicio 3")
nombre=input("Ingrese nombre: ")
apellido=input("Ingrese apellido: ")
edad=int(input("Ingrese edad: "))
residencia=input("Ingrese lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#ejercicio 4
print("Ejercicio 4")
radio=float(input("Ingrese radio:"))
area=math.pi*radio**2
perimetro=2*math.pi*radio
print(f"El área es {area} y el perímetro es {perimetro}")
#ejercicio 5
print("Ejercicio 5")
seg=int(input("Ingrese cantidad de segundos: "))
hora=seg/3600
print(f"La cantidad de horas son {hora}")
#ejercicio 6
print("Ejercicio 6")
n=int(input("Ingrese un número: "))
i=1
while i<11:
    a=i*n
    print(f"{i}*{n}={a}")
    i=i+1

#ejercicio 7
print("Ejercicio 7")
a=int(input("Ingrese primer número: "))
b=int(input("Ingrese segundo número: "))
s=a+b
r=a-b
m=a*b
d=a/b
print(f"{a}+{b}={s}, {a}-{b}={r}, {a}*{b}={m}, {a}/{b}={d}")

#ejercicio 8
print("Ejercicio 8")
altura=float(input("Ingrese su altura en metros: "))
peso=float(input("Ingrese su peso en kilogramos: "))
IMC=peso/(altura**2)
print(f"Su IMC es: {IMC}kg/m")

#ejercicio 9
print("Ejercicio 9")
Celsius=float(input("Ingrese temperatura en Celsius: "))
Fahrenheit=9/5*Celsius+32
print(f"Los {Celsius}°C = {Fahrenheit}°F")

#ejercicio 10
print("Ejercicio 10")
print("Ingrese 3 números") 
a=int(input())
b=int(input())
c=int(input())
promedio=(a+b+c)/3
print(f"El promedio de {a}, {b} y {c} es {promedio}")
