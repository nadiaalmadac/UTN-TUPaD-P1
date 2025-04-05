#Ejercicio 1
a=int(input("Ingrese edad "));
if (a>=18):
    print("Es mayor de edad");
#ejercicio 2
nota=int(input("Ingrese nota"));
if (nota>=6):
    print("Aprobado");
else: 
    print("Desaprobado");
#ejercicio 3
a=int(input("Ingrese número :"));
r=a%2;
if (r==0):
    print("Ha ingresado un número par");
else:
    print("Por favor, ingrese un número par")
#ejercicio 4
a=int(input("Ingrese edad :"));
if (a<12):
    print("Es un niño/a")
elif ((a>=12) and (a<18)):
    print("Es un adolescente/a")
elif ((a>=18) and (a<30)):
    print ("Es un adulto/a joven")
elif (a>=30):
    print ("Es un adulto/a ")

#ejercicio 5
n=len(input("Ingrese una contraseña:"))
if ((n<=14) and (n>=8)):
     print("Ha ingresado una contraseña correcta");
else: print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres");

#ejercicio 6
from statistics import mode, median, mean 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda=mode(numeros_aleatorios);
media=mean(numeros_aleatorios);
mediana=median(numeros_aleatorios);

if(media>mediana and mediana>moda):
    print("Sesgo positivo o a la derecha") 
elif (media<mediana and mediana<moda):
    print("Sesgo negativo o a la izquierda")
elif(media==moda and moda==mediana):
    print("Sin sesgo");
    
print("\n"); 
print(numeros_aleatorios);

#ejercicio 7
a=input("Ingrese una palabra o frase: ")
LU=a[len(a)-1]; #LU es la última letra de la frase.
if (LU=="a" or LU=="e" or  LU=="i" or LU=="o"or LU=="u" or LU=="A" or LU=="E" or LU=="I" or LU=="O" or LU=="U"):
    print(a+"!");
else: print(a);

#ejercicio 8
nombre=input("Ingrese nombre: ");
n=int(input("Ingrese 1,2,3 para imprimir su nombre:\n 1: MAYÚSCULAS \n 2: minúscula \n 3: Primer letra mayúscula:\n "));
if(n==1):
    print(nombre.upper());
elif(n==2):
    print(nombre.lower());
elif(n==3):
    print(nombre.title()); 

#ejercicio 9
n=float(input("Ingrese la magnitud de un terremoto: "));
if(n<3 and n>0):
    print("Muy leve");
elif(n>=3 and n<4):
    print("Leve");
elif(n>=4 and n<5):
    print("Moderado");
elif(n>=5 and n<6):
    print("Fuerte");
elif(n>=6 and n<7):
    print("Muy Fuerte");
elif(n>7):
    print("Extremo");

#ejercicio 10
dia=int(input("Ingrese el día de hoy: "))
mes=int(input("Ingrese el número de mes: \n1-Enero \n2-Febrero \n3-Marzo \n4-Abril \n5-Mayo \n6-Junio \n7-Julio \n8-Agosto \n9-Septiembre \n10-Octubre \n11-Noviembre \n12-Diciembre\n"));
hemisferio=input("Ingrese el hemisferio en el que se encuentra N/S: \n N:Norte \n S:Sur \n")
hemisferio=hemisferio.upper();
print(hemisferio)
if(mes==1 or mes==2):
    if(hemisferio=="N"):
        print("Usted está en Invierno")
    elif(hemisferio=="S"):
        print("Usted está en Verano")
elif(mes==4 or mes==5):
    if(hemisferio=="N"):
        print("Usted está en Primavera")
    elif(hemisferio=="S"):
        print("Usted está en Otoño")
elif(mes==7 or mes==8):
    if(hemisferio=="N"):
            print("Usted está en Verano")
    elif(hemisferio=="S"):
        print("Usted está en Invierno")
elif(mes==10 or mes==11):
    if(hemisferio=="N"):
        print("Usted está en Otoño")
    elif(hemisferio=="S"):
        print("Usted está en Primavera")
elif(mes==12):
    if(dia<=20 and dia>0):
        if(hemisferio=="N"):
               print("Usted está en Otoño")
        elif(hemisferio=="S"):
               print("Usted está en Primavera")
    elif(dia>=21 and dia<32):
         if(hemisferio=="N"):
               print("Usted está en Invierno")
         elif(hemisferio=="S"):
               print("Usted está en Verano")
elif(mes==3):
    if(dia<=20 and dia>0):
        if(hemisferio=="N"):
               print("Usted está en Invierno")
        elif(hemisferio=="S"):
               print("Usted está en Verano")
    elif(dia>=21 and dia<32):
        if(hemisferio=="N"):
               print("Usted está en Primavera")
        elif(hemisferio=="S"):
               print("Usted está en Otoño")
elif(mes==6):
    if(dia<=20 and dia>0):
        if(hemisferio=="N"):
               print("Usted está en Primavera")
        elif(hemisferio=="S"):
               print("Usted está en Otoño")
    elif(dia>=21 and dia<32):
        if(hemisferio=="N"):
               print("Usted está en Verano")
        elif(hemisferio=="S"):
               print("Usted está en Invierno")
elif(mes==9):
    if(dia<=20 and dia>0):
        if(hemisferio=="N"):
               print("Usted está en Verano")
        elif(hemisferio=="S"):
               print("Usted está en Invierno")
    elif(dia>=21 and dia<32):
        if(hemisferio=="N"):
               print("Usted está en Otoño")
        elif(hemisferio=="S"):
               print("Usted está en Primavera")
