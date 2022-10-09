# Tuple ()

# Aqui tenemos una variable la cual es una tupla, la cual es un conjunto de datos separados por "," con en forma de lista y encerrados dentro de un "()".

# Def Tuple var
tupla = (1,2,3,4,5)

print(tupla)
print(type(tupla))

# Como podriamos mostrar el primer valor?
print(tupla[0])

# y si intentaramos modificar la tuple esto es lo que conseguiriamos ya que no se puede por lo que es inmutable a diferencia de las litas...
tupla[1] = 10
print(tupla)
# Resultado: 
# TypeError: 'tuple' object does not support item assignment


