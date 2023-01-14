def multiplication_by_2(n):
    return n * 2

def add_2(n):
    return n + 2

def apply_operation(function, numbers):
    """ Aplica el tipo de operacion indica en la funcion pasada como argmunto y la aplica a la lista de nummber

    parametro function function defined
    parametro list numbers
    returns numbers con el tipo de operacion en funcion ingresada
    
    """
    
    results = []
    for number in numbers:
        result = function(number)
        results.append(result)
    return results


numbers = [1, 2, 3]
print(apply_operation(multiplication_by_2, numbers)) # Ingresamos como parametro la funcion de multiplicacion
print(apply_operation(add_2, numbers)) # Ingresamos como parametro la funcion de suma



print('Ejemplo de funciones lambda')
addition = lambda x, y : print(x + y)
addition(2,3)



print('Ejemplo de funciones en estructuras de datos')

def apply_operation(number):
    operations = [abs, float]
    results = []
    for operation in operations:
        results.append(operation(number))
    return results
print(apply_operation(-2))