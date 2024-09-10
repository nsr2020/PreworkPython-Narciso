""" Funciones 
1. Ejercicio: Define una función que tome dos números y retorne su suma. 
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo. 
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos. 
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa """


#1
def suma(a, b):
    return a + b
print("La suma de los números es:",suma(2,2))

#2

def factorial(a):
    fact = 1
    if a == 0:
        return 1
    if a < 0:
        return "Factorial no está definido para números negativos"
    
    while a > 0:
        fact *= a
        a -= 1
        
    return fact

print("El factorial del número introducido es:",factorial(5))

#3

def es_primo(n):
    divisor = 2
    n = int(n) #aqui me aseguro de que aunk pases decimales el número sea integer
    if n <= 1 :
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

""" num = int(input("introduce un numero entero: ")) """
if es_primo(11.25):
    print("El número es primo")
else:
    print("El número no es primo")


    #4
def sumaNums(listNums):
    suma = 0
    for num in listNums:
        suma += num
    return suma

print("La suma del listado de números es:",sumaNums([1,2,3,4,5]))

#5

def reverseString(str):
    return str[::-1]

print("La cadena en reversa es:", reverseString("Narciso"))