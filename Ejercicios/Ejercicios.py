# Ejercicios & Problems to solve with python:

# Ejercicio 1:
# construir la Tabla de la Disyuncion "or":

booleanos = [False, True]

print('X\t      Y\t     X or Y')
print('_'*26)

for X in booleanos:
  for Y in booleanos:
    print('{} \t {} \t {}'.format(X,Y,X or Y))






























