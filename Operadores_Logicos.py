# OPERADORES LOGICOS.......
# +*-=-
#-*+=-
#+*+=+
#-*-=+

# Operador "Not":

# Expresion verdadera:
resultado = 4 > 3
print(resultado)
# True

# El operador "Not" lo que hace es invertir el resultado "Bolean"
Resultado = not 4 > 3
print(Resultado)
# False



# Operador "And":
# Su funcion es de conjucion, es decir, de unir(union).

# Ejemplo Estructura 1:
resultado = 4 > 3 and 10 > 2
print(resultado)
# True

# Ejemplo Estructura 2:
# True and False = False
resultado = 4 > 3 and 10 < 2
print(resultado)
# Falso

# Ejemplo Estructura 3:
# False and True = False
resultado = 2 > 10 and 4 > 3
print(resultado)
# False

# Ejemplo Estructura 3:
# False and False = False
resultado = 2 > 10 and 4 < 3
print(resultado)
# False




# Operador "Or":
# Su funcion es de Disyuncion(Separar).

# Ejemplo Estructura 1:
year = 2022
altura = 1.80

Resultado = year == 2050 or altura > 1.20
print(Resultado)
# False year and altura True = True

# Ejemplo Estructura 2:
height = 1.20
year = 2050

solve_2 = height > 1.20 or year > 2022
print(solve_2)
# False year and altura True = True

# Ejemplo Estructura 3:
# <False_1> or <False_2> = False
height = 1.20
year = 2022

solve_3 = height < 1.20 or year < 2022
print(solve_3)
# False year and altura False = False


#________________________________________________________

# Ejemplo de logica:


#  E                               A
# pintar la Casa      ||      Bañarse
# <expresion_1>      ||      <expresion_2>

# Falsa             ^          Verdadera    

>>>> Falso



