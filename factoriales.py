# IMPORTANTE, es muy recomendado que cada vez que definimos una función lo primero que debemos hacer es escribir en un "docstring" que es lo que hace la función brevemente los parametros que recibe y los valores que devuelve la función
import sys
print(f'El limite de recursividad es: {sys.getrecursionlimit()}') # Con este modulo podemos averiguar el limite a nuestra recursividad
def factorial(input_factorial):
    """Calcula el factorial de n.

    n int > 0
    returns n!
    """
    print(input_factorial) # Aqui le seguimos el control al valor de "n"
    if input_factorial == 1:  # Primero hay que declarar nuestro caso base (hasta donde vamos a ir con nuestra iteracion) para evitar un "infinite loop" pero Python no permite eso cuando usamos "recursividad" solo nos mostrara un error
        return 1
    return input_factorial * factorial(input_factorial - 1) # En esta linea es donde invocamos la "recursividad"


input_factorial = int(input('Escribe un número: '))
print(f'El resultado factorial de {input_factorial} es {factorial(input_factorial)}')



# Aplicando recursividad en ejercicio de Fibonacci, poblacion de conejos (manera ineficiente)
n = int(input('Escribe un número: '))

def fibonacci(n):
    """Calcula la poblacion de conejos
    
    n int >= 0
    returns mes fibonacci
    """
    print(n)
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f'El número de fibonacci es: {fibonacci(n)}')



# Manera eficiente de fibonacci
n = int(input('Escribe un número: '))
fibonacci_cache = {}

def efficient_fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = efficient_fibonacci(n - 1) + efficient_fibonacci(n - 2)
    
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range (1, 1001):
    print (f'{n} : {efficient_fibonacci(n)}')



# Manera mucho más eficiente de realizar fibonacci usando recursividad y funciones importadas
from functools import lru_cache
@lru_cache(maxsize = 1000)

def most_efficient_fibonacci(n): 
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = most_efficient_fibonacci(n - 1) + most_efficient_fibonacci(n - 2)
    return value

for n in range (1, 1001):
    print (f'{n} : {most_efficient_fibonacci(n)}')















