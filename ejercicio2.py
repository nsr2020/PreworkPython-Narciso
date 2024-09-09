'''
1.1 Dado el siguiente diccionario cmabia el valor de la clave a 25
persona ={"nombre":"Paolo", "edad": 10}

1.2 Declara una variable precio y asignale el valor 25. Luego, crea una variable impuesto y asigna el valor
de precio multiplicado por 0.21
Muestra ambos valores por consola de esta forma:
El precio es 25 y el impuesto 5.25

1.3 Dado el siguiente diccionario, imprime con un print el valor de la clave apellido
persona = ["nombre":"Juan", "apellido":"Perez"]

1.4Crea un diccionario llamado producto que tenga las claves 'nombre','precio' y 'cantidad'
Asigna valores a estas claves y muestra el diccionario completo.
'''






#1.1

persona = {"nombre":"Paolo", "edad": 10}
persona["edad"] = 25
print(persona)

#1.2

precio = 25
impuesto = precio * 0.21
print("El precio es", precio, "y el impuesto", impuesto)

#1.3

persona2 = {'nombre':'Narciso', 'apellido':'Serrano'}
print(persona2['apellido'])

#1.4

producto = {"nombre":"Laptop", "precio":750, "cantidad":3}
print(producto)