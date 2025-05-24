#Ejercicio 1
def imprimir_hola_mundo():
     print("Hola mundo!.")


imprimir_hola_mundo()

#Ejercicio 2

def saludar_usuario(nombre):
     print(f"Hola {nombre}!")

a=input("Ingrese su nombre:")

saludar_usuario(a)

#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}" )
           
n=input("Nombre: ")     
ap=input("Apellido: ")
e=input("Edad: ")
r=input("Residencia: ")

informacion_personal(n,ap,e,r)


#Ejercicio 4
import math

def calcular_area_circulo(radio):
     return math.pi*radio**2
def calcular_perimetro_circulo(radio):
     return 2*math.pi*radio

r=float(input("Ingrese el radio: ")) 
A=calcular_area_circulo(r)
P=calcular_perimetro_circulo(r)
print(f"El área del círculo con radio {r} es {A} y el perímetro es {P}")

#Ejercicio 5
def segundos_a_horas(segundos):
     return segundos/3600

s=int(input("Ingrese la cantidad de segundos: "))
h=segundos_a_horas(s)
print("La cantidad de horas son: "+h)

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(11):
        a=i*numero
        print(f"{i}x{numero}={a}")


num=int(input("ingrese un número: "))

tabla_multiplicar(num)

#Ejercicio 7
def operaciones_basicas(a, b):
    print("La suma es: ",a+b)
    print("La resta es: ", a-b)
    print("La múltiplicación es: ", a*b)
    print("La división es: ", a/b)

print("Ingrese dos números separados por un enter: ")
num_1=int(input())
num_2=int(input())
operaciones_basicas(num_1,num_2)

#Ejercicio 8
def calcular_imc(peso, altura):
    IMC=peso/((altura)**2)
    if (IMC>0):
        if(IMC<18.5):
            print("Tiene bajo peso")
        elif(IMC<25):
            print("Tiene peso normal")
        elif(IMC<30):
            print("Tiene sobrepeso")
        elif(IMC<35):
            print("Tiene obesidad")
        else:
            print("Tiene obseidad extrema")
    else:
        print("Ingrese obesidad extrema")


p=float(input("Ingrese el peso en kilogramos: "))
e=float(input("Ingrese estatura en metros: "))    
calcular_imc(p,e)


#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return ((celsius*1.8)+32)

C=float(input("Ingrese los grados en Celsius: "))
print(celsius_a_fahrenheit(C))

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a+b+c)/3
print("Ingrese tres números separados por enter: ")
n1=float(input())
n2=float(input())
n3=float(input())
print(calcular_promedio(n1,n2,n3))