x = 'Esta es una variable global'

def local_variable():
    x = 'Y esta es una variable local'
    print(x)

print(x)
local_variable()
