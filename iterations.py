"""contador = 0

while contador < 10:
    print(contador)
    contador += 1 # Forma abreviada de 'contador = contadaro + 1' """

outer_counter = 0
inner_counter = 0

while outer_counter < 5:
    while inner_counter < 6:
        print(outer_counter, inner_counter)
        inner_counter += 1

        if inner_counter >= 3:
            break

    outer_counter += 1
    inner_counter = 0