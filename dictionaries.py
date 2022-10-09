# Dictionaries in Python:

# Dict{}

# Se pone el supuesto que vayamos a crear un programa en el que se vaya a analizar los datos de un grupo de estudiantes.

# Nota: seria muy complicado hacerlo con variables ya que solo pueden alamacenar una cadena o un numero determinado. (datos primitivos)

# entonces con un diccionario vamos a pasarle toda informacion que tendria un estudiante dentro del programa.

# Le pasamos un nombre a la declaracion de la variable del diccionario, y los diccionarios se reconocen porque estan dentro de corchetes, para contener dentro la informacion. Entre cadena de caracter formamos una especie de lista.

# De esta forma también es que se crean los archivos de objetos en formato "Json" para las APIs por ejm, e incluso los Schemas de bases de datos

Student = {
  'Name': "Brian Parker",
  'Age': 19,
  'Sex': "M",
  'Calification': 4.5,
  'currentStatus': True
}

# NOTA: Los diccionarios son como un grupo de variables dentro de un contenedor en donde la 'Key' es el nombre de la variable, "Value" es el valor almacenado en su interior.

# Nota: para este caso tenemos 5 elementos como "Keys" nombre, edad, genero, nota y estado. Donde cada una se comporta igual que una variable, tiene un nombre y almacena un valor. Pero se encapsula o incluye dentro de una variable "global" mas grande.

print(Student)
print(type(Student))

# Mostrar el valor de una "Key" de este 'dict' diccionario

print(Student['Name'])

# print todo el diccionario en una Lista
# Aprovechandonos de la función que traen los diccionarios en Python.
print(Student.items())

# Entonces, Cuando se utilizan?

# Cuando tenemos muchos datos y necesitamos agruparlos en dos conjuntos de elementos: "Key" & "Value". Clave y valor.

















