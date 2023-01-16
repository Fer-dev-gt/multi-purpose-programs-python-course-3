import time

objetivo = int(input('Ingresa un número: '))
# Con esta asignacion medimos el tiempo que tarda la computadora en hacer el calculo
initial_time = time.time()
epsilon = 0.01 # Epsilon nos ayuda a definir que tan preciso queremos ser
paso = epsilon ** 2 # La respuesta es 0.0001, incrementara "response" poco a poco
response = 0.0

while abs(response ** 2 - objetivo) >= epsilon and response <= objetivo:
    # IMPORTANTE, cuando no entendamos muy bien que esta haciendo nuestro codigo, recuerta que la funcion "print()" es tu amigo y te ayuda a saber como se estan procesando los datos
    print(abs(response ** 2 - objetivo), response) 
    response += paso

if abs(response ** 2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {response}')

print(f'El programa se tardo {time.time() - initial_time} segundos en completarse')
