import random

transfer_hours = random.randint(0,24)
print(f'La hora actual es: {transfer_hours}')

client_bank = 'Banrural'
client_account = int(input('Ingresa tu numero de cuenta: '))
client_balance = 1000000
transfer = int(input(f'Tu saldo actual es de {client_balance}, ¿Cuanto deseas transferir? '))

receiving_bank = input('¿A que banco vas a transferir dinero? ')
receiving_account = int(input('Ingresa el numero de la cuenta que recibira la transferencia: '))

# Se realiza calculos y transferencia
def send_transfer(total_transfer, client_balance):
    new_balance = client_balance - total_transfer
    print(f'Tu transaccion con valor a USD{total_transfer} a la cuenta {receiving_account} se realizo exitosamente')
    print(f'El saldo de tu cuenta #{client_account} ahora es de {new_balance}')

# Forma con condicionales anidados
if transfer_hours >= 9 and transfer_hours <= 12 or transfer_hours >= 15 and transfer_hours <= 20: 
    if client_account != receiving_bank:
        if client_account != receiving_bank:
            print('Al ser la otra cuenta del mismo banco no hay costo de transaccion')
            transaction_cost = 0
            total_transfer = transfer + transaction_cost
            send_transfer(total_transfer, client_balance)
        else:
            print('La transferencia a otros bancos tiene un costo de transaccion de USD 100')
            transaction_cost = 100
            total_transfer = transfer + transaction_cost
            if client_balance >= total_transfer:
                send_transfer(total_transfer, client_balance)
            else:
                print('Fondos insuficientes para transaccion')
    else:
        print('Numero de cuenta no existe en el banco')
else:
    print('El horarario de transferencias es de 9 a 12 y de 15 a 20, intentalo más tarde')


# Forma de hacer con las condicionales en una sola linea, pendiente mensaje cuando no se cumple la condicional
if (transfer_hours >= 9 and transfer_hours <= 12 or transfer_hours >= 15 and transfer_hours <= 20) and (client_account != receiving_bank) and (client_account != receiving_bank):
    print('\nAl ser la otra cuenta del mismo banco no hay costo de transaccion')
    transaction_cost = 0
    total_transfer = transfer + transaction_cost
    send_transfer(total_transfer, client_balance)

