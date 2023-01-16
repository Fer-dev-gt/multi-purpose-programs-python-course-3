"""IMPORTANTE: para que la busqueda binaria funcione el requisito fundamento es que nuestro recurso de busqueda este ordenado, tiene que existir un order, por ejemplo los numero"""

objetivo = int(input('Ingresa un número: '))
epsilon = 0.0000001 # Con este algoritmo podemos ser más precisos con "epsilon"
bajo = 0.0 # Limite inferior
alto = max(1.0, objetivo) # Limite superior
response = (alto + bajo) / 2 # Valor que luego asignaremos a limite bajo o alto dependio del condicional

# Ciclo while que itera con el valor de "response" y lo asigna a "bajo" o "alto" dependiendo de la condicional
while abs(response ** 2 - objetivo) >= epsilon:
    print(f'bajo = {bajo}, alto = {alto}, respuesta = {response}')
    
    if response ** 2 < objetivo:
        # Asigna cual sera el limite inferior
        bajo = response
    else:
        # Asigna cual sera el limite superior
        alto = response
    response = (alto + bajo) / 2
print(f'La raiz cuadrada de {objetivo} es {response}')


"""Un buen consejo trata de que si no tenemos una forma muy logica de encontrar la respuesta, nuestra mejor opcion es probar todas las soluciones con la 'Enumeración Exhaustiva'"""