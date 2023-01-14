# Solicitud datos del primer usuario
name_user_1 = input('¿Cual es tu nombre? ')
age_user_1 = int(input(f'Gusto en conocerte {name_user_1}, ahora dime cuantos años tienes: '))

# Solicitud datos segundo usuario
name_user_2 = input('\nIngresa el nombre del otro usuario: ')
age_user_2 = int(input('¿Cual es la edad del otro usuario? '))

print('\nA continuación te diré que usuario es mayor...')

# Uso de condicional para definir que usuario es mayor que el otro
if age_user_1 > age_user_2:
    print(f'El usuario {name_user_1} es mayor al usuario {name_user_2}')
elif age_user_1 < age_user_2:
    print(f'El usuario {name_user_2} es mayor al usuario {name_user_1}')
else:
    print(f'Me parece que {name_user_1} y {name_user_2} tienen la misma edad, interesante...')

