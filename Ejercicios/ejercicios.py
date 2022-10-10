# Ejercicios & Problems to solve with python:

# Ejercicio 1:
# construir la Tabla de la Conjucion "&":

booleanos = [False, True]

print('X\t      Y\t     X & Y')
print('_'*26)

for X in booleanos:
  for Y in booleanos:
    print('{} \t {} \t {}'.format(X,Y,X & Y))

# Ejercicio 2:
# construir la Tabla de la Disyuncion "or":

booleanos = [False, True]

print('X\t      Y\t     X or Y')
print('_'*26)

for X in booleanos:
  for Y in booleanos:
    print('{} \t {} \t {}'.format(X,Y,X or Y))

# Ejercicio 3:
# construir la Tabla de la Negacion "not":

booleanos = [True, False]

print('X   not   X')
print('_'*26)

for X in booleanos:
  print('{} \t {}'.format(X, not X))




















