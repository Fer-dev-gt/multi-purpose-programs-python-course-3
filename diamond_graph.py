lenght_diamond = int(input('¿De qué longitud quieres que sea el diamante? '))
counter = 0
lower_part = lenght_diamond

# Grafica de parte superior del diamante
while lenght_diamond > 0:
    draw = '*' * lenght_diamond
    print(draw + ' ' * counter + draw)
    lenght_diamond -= 1
    counter += 2

counter -= 2
lenght_diamond = 1

# Grafica de parte inferior del diamante
while lenght_diamond < lower_part + 1:
    draw = '*' * lenght_diamond
    print(draw + ' ' * counter + draw)
    lenght_diamond += 1
    counter -= 2

print(iter({'primero' : 1 , 'segundo' : 2}))
print(iter(['a', 'b', 'c']))
print(iter({'col','bol','gua'}))
print(iter(('natacion', 'boxeo', 'ciclismo')))

noiterable = 1
print(iter(noiterable))