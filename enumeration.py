import time

objective = int(input('Escoge un número entero: '))
# Con esta asignacion medimos el tiempo que tarda la computadora en hacer el calculo
initial_time = time.time()
response = 0

while response ** 2 < objective:
    print(response)
    response += 1

if response ** 2 == objective:
    print(f'La raiz cuadrada de {objective} es: {response}')
else:
    print(f'El número {objective} no tiene raiz cuadrada exacta')

# Hacemos calculo para saber cuanto tiempo le como completar el calculo 
print(f'El programa se tardo {time.time() - initial_time} segundos en completarse')