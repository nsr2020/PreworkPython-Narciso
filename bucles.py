""" Bucles 
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for. 
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while. 
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100. """

#1

numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

#2

cont = 1
while cont <= 20:
    if cont % 2 == 0:
        print(cont)
    cont += 1

#3
sum = 0
num = 1
while num <=100:
    sum += num
    num += 1
print(f"La suma de los numeros del 1 al 100 es: {sum}")    