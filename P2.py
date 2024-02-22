import sys

""" PROBLEMA 9 """

#print(ord('A'))

""" PROBLEMA 10 """

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

print("suma de los numeros: " (num1 + num2 + num3))
print("promedio de los numeros: " (num1 + num2 + num3)/3)
print("producto de los numeros: " (num1 * num2 * num3))

mayor = num1
medio = num2
menor = num3

if num2 > mayor:
    mayor = num2
    medio = num1
    menor = num3

if num3 > mayor:
    mayor = num3
    medio = num1
    menor = num2
elif num3 > medio:
    medio = num3
    menor = num2

print("Orden: {}, {}, {}".format(mayor, medio, menor))


""" PROBLEMA 11 """

n = int(input("Ingresa un numero: "))

d1 = n // 10000
d2 = n // 1000 % 10
d3 = n // 100 % 10
d4 = n // 10 % 10
d5 = n % 10 

print(d1, d2, d3, d4, d5)

""" PROBLEMA 12 """

rentabilidad = 0.7
saldo = 100000

monto1 = saldo(1 + rentabilidad)**10
monto2 = saldo(1 + rentabilidad)**20
monto3 = saldo(1 + rentabilidad)**30


""" PROBLEMA 13 """
sys.set_int_max_str_digits(1000000)

numero = int(input("Ingresa un numero: "))
print(numero)


""" PROBLEMA 14 """

numero = int(input("Ingrese un numero para regresar el ultimo digito: "))

ultimo_digito = numero % 10

print("El ultimo digito del numero", numero, "es", ultimo_digito)


""" PROBLEMA 15 """

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

numero_menor = numero1

if numero2 < numero_menor:
    numero_menor = numero2

if numero3 < numero_menor:
    numero_menor = numero3

print("El numero menor es:", numero_menor)


""" PROBLEMA 16 """

numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")
numero3 = input("Ingrese el tercer numero: ")

if numero1 == numero2 == numero3:
    print(f"Los valores {numero1}, {numero2} y {numero3} son iguales.")
else:
    print(f"Los valores {numero1}, {numero2} y {numero3} no son iguales.")


""" PROBLEMA 17 """

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

if num1 < num2:
    if num1 < num3:
        min_num = num1
        if num2 < num3:
            mid_num = num2
            max_num = num3
        else:
            mid_num = num3
            max_num = num2
    else:
        min_num = num3
        mid_num = num1
        max_num = num2
else:
    if num2 < num3:
        min_num = num2
        if num1 < num3:
            mid_num = num1
            max_num = num3
        else:
            mid_num = num3
            max_num = num1
    else:
        min_num = num3
        mid_num = num2
        max_num = num1

print("Los numeros en orden creciente son:", min_num, ",", mid_num, "y", max_num)


""" PROBLEMA 18 """

total_huevos = 28

huevos_obtenidos = int(input("Ingrese la cantidad de huevos obtenidos: "))

tamano_cartera = 6

cajas_necesarias = huevos_obtenidos // tamano_cartera

huevos_ultima_cartera = huevos_obtenidos % tamano_cartera

huevos_adicionales = tamano_cartera - huevos_ultima_cartera

print("Cantidad de cajas necesarias:", cajas_necesarias)
print("Huevos en la ultima cartera:", huevos_ultima_cartera)
print("Huevos adicionales necesarios para llenar la ultima cartera:", huevos_adicionales)
