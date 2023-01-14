
objective = int(input('Escoge un número entero para calcularle su raíz cuadrada: '))
choice_method = int(input('Escoge entre los siguintes métodos con el que quieres que se realice el calculo; \n1) Método por enumeración exhaustiva \n2) Método por aproximación \n3) Método por busqueda binaria \n'))
response = 0
epsilon = 0.0001

def enumeration(objective):
    """ Calcula raiz cuadrada de "objective" usando enumeracion exhaustiva
        objective int > 0
        returns raiz cuadrada en variable "response"
    """
    while response ** 2 < objective:
        print(response)
        response += 1

    if response ** 2 == objective:
        print(f'La raiz cuadrada de {objective} es: {response}')
    else:
        print(f'El número {objective} no tiene raiz cuadrada exacta')

def aproximation(objective, epsilon):
    paso = epsilon ** 2
    response = 0.0

    while abs(response ** 2 - objective) >= epsilon and response <= objective:
        print(abs(response ** 2 - objective), response) 
        response += paso

    if abs(response ** 2 - objective) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objective}')
    else:
        print(f'La raiz cuadrada de {objective} es {response}')


def binary_search(objective, epsilon):
    bajo = 0.0 
    alto = max(1.0, objective) 
    response = (alto + bajo) / 2 

    while abs(response ** 2 - objective) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {response}')

        if response ** 2 < objective:    
            bajo = response
        else:
            alto = response

        response = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objective} es {response}')



if choice_method == 1:
    print('Calculando usando Enumeración Exhaustiva')
    enumeration(objective, response)
elif choice_method == 2:
    print(f'Calculando usando Aproximacion con margen de error de: {epsilon}')
    aproximation(objective, epsilon)
elif choice_method == 3:
    print(f'Calculando usando Busqueda Binaria con margen de error de: {epsilon}')
    binary_search(objective, epsilon)
else:
    print("Escoge un método de calculo valido (1, 2 o 3)")