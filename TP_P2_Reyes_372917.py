# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 07:26:32 2024

@author: Reyes Varela Salvador Isaac ~ 372917

"""

""" 

Practica No. 2 de Python

"""

""" PROBLEMA 1 """

import str

x = 2
y = 3
print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), 'x =', (y + x))


#imprime el valor de x al realizar operaciones basicas con la variable



""" PROBLEMA 2 """

calificacion = input('Ingrese una calificacion entera entre 1 y 100: ')

 
#puedes ingresar cualquier valor que no sea entero en la variable "calificacion", se demuestra al
#imprimir la variable



""" PROBLEMA 3 """

calificacion = int (input('Ingrese una calificacion entera entre 1 y 100: ') )
if calificacion >= 90:
    print('Felicitaciones! Tu calificación de ',  calificacion,' te otorga una A en este curso')


""" PROBLEMA 4 """

radio = 6
pi = 3.1416

diametro = 2 * radio
print(diametro)

circunferencia = 2 * pi * radio
print(circunferencia)

area = pi * radio**2
print(area)

""" PROBLEMA 5 """

n = int (input("Ingrese un numero entero para verificar si es par o impar: "))

if n % 2 == 0:
    print("El numero ", n, " es par")

if n % 2 != 0:
    print("El numero ", n, " es impar")
    


""" PROBLEMA 6 """

n1 = int(input("Ingrese el primer numero entero: "))

n2 = int(input("Ingrese el segundo numero entero: "))

if n1 % n2 == 0:
    print(n2, " es un multiplo de ", n1)

if n1 % n2 != 0:
    print(n2, " no es un multiplo de ", n1)


""" PROBLEMA 7 """

print('numero', '\t', 'cuadrado', ' ', 'cubo')
print(0, '\t\t', 0, ' \t\t', 0)
print(1, '\t\t', 1**2, ' \t\t', 1**3)
print(2, '\t\t', 2**2, ' \t\t', 2**3)
print(3, '\t\t', 3**2, ' \t\t', 3**3)
print(4, '\t\t', 4**2, ' \t\t', 4**3)
print(5, '\t\t', 5**2, ' \t\t', 5**3)

""" PROBLEMA 8 """


print('numero'.rjust(2), '\t', 'cuadrado'.rjust(2), ' ', 'cubo'.rjust(2))
print(str(0).rjust(6), str(0).rjust(10), str(0).rjust(6))
print(str(1).rjust(6), str(1**2).rjust(10), str(1**3).rjust(6))
print(str(2).rjust(6), str(2**2).rjust(10), str(2**3).rjust(6))
print(str(3).rjust(6), str(3**2).rjust(10), str(3**3).rjust(6))
print(str(4).rjust(6), str(4**2).rjust(10), str(4**3).rjust(6))
print(str(5).rjust(6), str(5**2).rjust(10), str(5**3).rjust(6))
