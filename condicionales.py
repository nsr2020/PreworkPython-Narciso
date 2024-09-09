""" 
Condicionales 
1. Ejercicio: Dado un número, imprime si es positivo o negativo. 
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos. 
"""


#1
num = -5
if num >= 0:
    print(f'{num} es positivo')
else:
    print(f'{num} es negativo')

#2
num2 = 3
if num2 % 2 == 0:
    print(f'{num2} es par')
else:
    print(f'{num2} es impar')       

#3
n1 = 80 
n2 = 10
n3 = 111
if n1 > n2 and n1 > n3:
    print(f'{n1} es el mayor')
elif n2 >n3 and n2 > n1:
    print(f'{n2} es el mayor')
else:
    print(f'{n3} es el mayor')        