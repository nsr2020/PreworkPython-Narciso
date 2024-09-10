""" Bucles y Funciones Ejercicios nivel medio 
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci. 
2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores. 
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original. 
4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos. 
5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena. 
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista. 
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena. 
8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3. 
9. Ejercicio: Define una función que reciba un número y retorne su representación en binario. 
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas). 
11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). 
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”. 
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada enorden ascendente. 
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n. 
15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci. 
16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista. 
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo. 
18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False. 
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso. 
21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene. 
22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números 
23. Ejercicio: Define una función que encuentre el elemento más común en una lista. 
24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10. 
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena. 
26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas. 
27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados. 
28. Ejercicio: Define una función que reciba un número entero positivo y retorne lasuma de los cuadrados de todos los números pares menores o iguales a ese número. 
29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista. 
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista. 
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos. 
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso. 
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla. 
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena. 
35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False. """

#1Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci. 

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print("Los primeros números de la secuencia son:", fibonacci(13))

#2Ejercicio: Define una función que tome un número y retorne una lista de sus divisores. 

def divisors(num):
    divisors_list = []
    x = 1
    while x < num:
        if num % x == 0:
            divisors_list.append(x)
        x += 1
    return divisors_list

n = 10

print("Los divisores de", n, "son:", divisors(n))

#3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.

def unique_elements(lst):
    return list(set(lst))

lst = [1, 2, 3, 3, 4, 5, 5, 6]

print("La lista sin duplicados es:", unique_elements(lst))

#4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.

def sum_digits(num):
    total = 0
    num_string =str(num)
    for digit in num_string:
        total += int(digit)
    return total    

n = 123410

print("La suma de los dígitos de", n, "es:", sum_digits(n))

#5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1

    return count

string = "Hello World"

print("La cadena", string, "contiene", count_vowels(string), "vocales.")    

#6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.

def first_n_elements(lst, n):
    return lst[:n]

lst = [1, 2, 3, 4, 5, 6]
n = 6

print("Los primeros", n, "elementos de la lista son:", first_n_elements(lst, n))

#7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.

def count_case_letters(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        if char.islower():
            lower_count += 1
    return upper_count, lower_count

string = "Hello World"

upper_count, lower_count = count_case_letters(string)

print("La cadena", string, "contiene", upper_count, "letras mayúsculas y", lower_count, "letras minúsculas.")  

#8.Ejercicio: 
# Define una función que tome un número y retorne True si es un número perfecto, 
# False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. 
# Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3. 

def is_perfect_number(num):
    if num < 2:
        return False
    sum_divisors = 1
    i= 2
    while i * i <= num:
        if num % i == 0:
            sum_divisors += i + num // i
        i += 1
    return sum_divisors == num    

num = 8

print(num, "¿es un número perfecto? :", is_perfect_number(num))

#9. Ejercicio: Define una función que reciba un número y retorne su representación en binario. 

def binary_representation(num):
    return bin(num)[2:]

n = 10

print("La representación en binario de", n, "es:", binary_representation(n))


# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas 
# (los elementos que están en las dos listas). 

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

print("La intersección de", lst1, "y", lst2, "es:", intersection(lst1, lst2))

#11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo 
# (se lee igual de izquierda a derecha que de derecha a izquierda). 

def is_palindrome(string):
    return string == string[::-1]

string = "HOla"

print(string, "¿es un palíndromo? :", is_palindrome(string))

#12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, 
# pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. 
# Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”. 

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente. 

def sort_list(lst):
    return sorted(lst)

lst = [5, 2, 8, 1, 3, 6]

print("La lista ordenada ascendente es:", sort_list(lst))


#14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, 
# y retorne la lista de palabras que son más largas que n. 

def long_words(lst, n):
    result = []
    for word in lst:
        if len(word) > n:
            result.append(word)
    return result        

lst = ["apple", "banana", "cherry", "date", "elderberry"]
n = 5

print("Las palabras más largas de", n, "caracteres son:", long_words(lst, n))


#15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci. 

def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = 10

print("La serie de Fibonacci de los primeros", n, "números es:", fibonacci(n))

#16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista. 

def max_number(lst):
    return max(lst)

lst = [5, 2, 8, 1, 3, 6]

print("El número más grande de la lista es:", max_number(lst))


#17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo. 

def sum_of_cubes(num):
    total = 0
    num_string = str(num)
    for digit in num_string:
        total += int(digit) ** 3
    return total

n = 12345

print("La suma de los cubos de los dígitos de", n, "es:", sum_of_cubes(n))

#18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.

def secondMaxNumber(list):
    sorted_list = sorted(list)
    secondBigNumber = sorted_list[-2]
    return secondBigNumber

list = [7, 2, 8, 1, 3, 6]

print("El segundo número más grande de la lista es:", secondMaxNumber(list))

#19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, 
# de lo contrario, retorne False. 

def common_elements(lst1, lst2):
    return bool(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 10, 9]
lst2 = [4, 5, 6, 7, 8]

print("Las listas tienen algún miembro en común?", common_elements(lst1, lst2))

#20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original 
# en orden inverso. 

def reverse_list(lst):
    return lst[::-1]

lst = [1, 2, 3, 4, 5]

print("La lista invertida es:", reverse_list(lst))

#21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene. 

def count_characters(string):
    digit_count = 0
    letter_count = 0
    for char in string:
        if char.isdigit():
            digit_count += 1
        if char.isalpha():
            letter_count += 1
    return digit_count, letter_count

string = "Hello World! 123"

digit_count, letter_count = count_characters(string)

print("La cadena", string, "contiene", digit_count, "dígitos y", letter_count, "letras.")

#22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números 

def cumulative_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

lst = [1, 2, 3, 4, 5]

print("La suma acumulada de los números en la lista es:", cumulative_sum(lst))


#23. Ejercicio: Define una función que encuentre el elemento más común en una lista. 

def find_common_element(lst):
    if len(lst) == 0:
        return None
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

lst = [1, 2, 2, 1, 2, 3, 4, 5]

common_element = find_common_element(lst)

if common_element is None:
    print("No hay elementos comunes en la lista.")
else:
    max_count = max(common_element.values())
    common_elements = [num for num, count in common_element.items() if count == max_count]
    print("El elemento más común en la lista es:", common_elements[0])    

#24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar 
# de ese número del 1 al 10. 

def multiplication_table(num):
    result = {}
    for i in range(1, 11):
        result[i] = num * i
    return result

num = 5

multiplication_table = multiplication_table(num)

print("La tabla de multiplicar del número", num, "es:", multiplication_table)

#25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones
# de cada caracter en la cadena. 

def count_characters(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1    
    return result

string = "Hello World!"

character_count = count_characters(string)

print("La cantidad de apariciones de cada caracter en la cadena", string, "es:", character_count)

#26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas. 

def find_unique_elements(lst1, lst2):
    unique_elements = []
    for num in lst1:
        if num not in lst2:
            unique_elements.append(num)
    for num in lst2:
        if num not in lst1:
            unique_elements.append(num)        
    return unique_elements

lst1 = [1, 2, 3, 4, 5]

lst2 = [4, 5, 6, 7, 8]

unique_elements = find_unique_elements(lst1, lst2)

print("Los elementos que no están en ambas listas son:", unique_elements)

#27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados. 

def remove_duplicates(lst):
    unique_elements = set(lst)
    return unique_elements

lst = [1, 2, 3, 2, 4, 5, 1]

unique_elements = remove_duplicates(lst)

print("La lista sin duplicados es:", unique_elements)

#28. Ejercicio: Define una función que reciba un número entero positivo y retorne lasuma de los cuadrados 
# de todos los números pares menores o iguales a ese número. 

def sum_of_squares(n):
    total = 0
    for num in range(2, n+1, 2):
        total += num ** 2
    return total

n = 10

print("La suma de los cuadrados de los números pares menores o iguales a", n, "es:", sum_of_squares(n))


#29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista. 

def calculate_average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

lst = [1, 2, 3, 4, 5]

average = calculate_average(lst)

print("El promedio de los números en la lista es:", average)

#30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista. 

def find_longest_string(lst):
    longest_string = ""
    for string in lst:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

lst = ["Hello", "Worlddddd", "This", "is", "a", "test"]

longest_string = find_longest_string(lst)

print("La cadena más larga en la lista es:", longest_string)

#31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos. 

def generate_prime_numbers(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

n = 10

prime_numbers = generate_prime_numbers(n)

print("Los primeros", n, "números primos son:", prime_numbers)

#32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.

def reverse_words(string):
    words = string.split()
    print(words)
    reversed_words1 = words[::-1]
    print(reversed_words1)
    reversed_string = " ".join(reversed_words1)
    print(reversed_string)
    return reversed_string 

string = "Hello World!"

reversed_string = reverse_words(string)

print("La cadena con las palabras en orden inverso es:", reversed_string)


#33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada 
# en el último elemento de cada tupla. 

def sort_tuples(lst):
    return sorted(lst, key=lambda x: x[-1])

lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

sorted_lst = sort_tuples(lst)

print("La lista ordenada según el último elemento es:", sorted_lst)

#34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena. 

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = "Hello World!"

vowel_count = count_vowels(string)

print("La cadena", string, "contiene", vowel_count, "letras vocales.")


#35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, 
# de lo contrario retorne False. """

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    

n = 9

is_prime_result = is_prime(n)

print("El número", n, "es primo:", is_prime_result)   




    




