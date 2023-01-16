def divide_elementos_de_lista(lista, divisor):
    try:  # el "try" es para probar una expresion para ver si hay un error de cualquier tipo
        return [i / divisor for i in lista]
    except ZeroDivisionError as error: # Indicamos el posible tipo de error que puede aparecer, en este caso la posible division de 0
        print(error) # Imprimimos que tipo de error detectó
        return lista


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))