# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 09:26:36 2023

@author: Cesar Perez
"""


#*********EJEMPLOS CAPITULO 8*************



#****Ejemplo 8.4*****

#FORMULA GENERAL

"""

#Funcion que calcula el discriminante

def discriminante(a1,b1,c1):
    d=math.sqrt((b1*b1)-4*a1*c1)
    
    print(d)
    
    return d


import math

#Entrada de datos

a=float(input("Dame el coheficiente de x**2: "))
b=float(input("Dame el coheficiente de x: "))
c=float(input("Dame el termino independiente: "))

#La variable d1 guardara la funcion discriminante()

d1=discriminante(a, b, c)


#Calculo de raices

x1=(-b+d1)/2/a

x2=(-b-d1)/2/a

print("La raiz x1 es: ", x1)
print("La raiz x2 es: ",x2)



#Ejemplo 8.4 forma 2

#Funcion que recibe los datos

def lectura():    
    a=float(input("Dame el coheficiente de a: "))
    b=float(input("Dame el coheficiente de b: "))
    c=float(input("Dame el termino c: "))
    
    return[a,b,c]  #Se guardan en una lista


#Funcion que realiza los calculos

def calcular(a,b,c,d):
    x1=(-b+d)/2/a
    x2=(-b-d)/2/a
    
    return(x1,x2)


#Llama a la funcion lectura()
[a,b,c]= lectura()

#Llama a la funcion discriminante() sino se pone no hay problema ya que ya esta calculado 
#y llamado arriba

d1=discriminante(a,b,c)

(x1,x2)=calcular(a, b, c, d1)

print("La primera raiz es: ",x1)

print("La segunda raiz es: ",x2)

"""

#*****Ejemplo 8.7******

#CALCULO FACTORIAL

"""

#funcion que calcula el factorial
def factorial (n):
    fact=1              #contador
    for k in range(2,n+1):      #fact tomara el valor de multiplicar fact*k
        fact=fact*k
        
        print(fact)
        
    return fact

print("Dame un numero entero: ")
numero=int(input())

factor=factorial(numero)

print("El factorial del numero ", numero,"es ", factor)


"""

#*****Ejemplo 8.12******

#SERIE FIBONACCI

"""
#Proceso que calculara la serie fibonacci 
def fibonacci(m):
    f0=0
    f1=1
    lista_fibo=[0,1]
    
    
    for k in range(2,m):        #Todo esteproceso cambia los valores de f0,f1 y f 
                                #conforme vaya aumentando el contador
        f=f0+f1
        f0=f1
        f1=f
        lista_fibo.append(f)
        
    print("La serie Fibonacci es: ",lista_fibo)
    
    
fibonacci(10)
"""

#****Ejemplo 8.13******

"""
#Recibe las variables del programa principal
def modificar (a,b,c):
    a=a+3
    b=b+3
    c=c+3
    suma=a+b+c
    
    return a,suma

#proceso que regresa el resultado
def escribir(suma):
    print("La suma es: ",suma)
    
#programa principal
a=1; b=2.3; c=7.1

[suma,a]=modificar(a, b, c)
escribir(suma)

print("El valor de a es: ", a)

"""

#*****Ejemplo 8.14*****


#Funcion suma de digitos
def adicion(caso):
    suma=0
    for k in range(caso):
        suma=suma+lista_digitos[k]
        
    return suma


#Funcion que realiza multiplicacion de digitos
def multiplicacion(caso):
    producto=1
    for k in range(caso):
        producto=producto*lista_digitos[k]
        
    return producto

#Funcion que delimita el rango 

def digitos(numero):
    global lista_digitos
    if (numero<=10):
        caso=1
    elif(numero<=100):
        caso=2
    elif(numero<=1000):
        caso=3
    elif(numero<=10000):
        caso=4
    elif(numero<=10000):
        caso=5
    else:
        caso=6
        
    for k in range(caso):
        
        lista_digitos.append(numero%10)  #Obtencion del residuo
        numero=numero//10               #Obtencion del cociente
        
        
        #Los digitos estan almacenados en el vector lista_digitos[k]
        #El numero de digitos es el valor del caso
        
    return caso



#Funcion que compara los resultados de las funciones adicion y multiplicacion
def comparacion(suma,producto):
    resultado= False
    if(suma==producto):
        resultado=True
        
    return resultado

#Programa principal
lista_digitos=[]

print("Dame un numero: ")
numero=int(input())

caso=digitos(numero)
print("Lista digitos ", lista_digitos)

suma=adicion(caso)
producto=multiplicacion(caso)
resultado=comparacion(suma, producto)

if(resultado):
    print("El numero cumple la condicion")
else:
    print("El numero no cumple la condicion")    
    







    


    




                