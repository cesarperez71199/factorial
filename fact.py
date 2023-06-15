# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 09:26:36 2023

@author: Cesar Perez
"""
#CALCULO FACTORIAL

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
