# Abrir y manipular archivo

mi_archivo = open('prueba.txt') # abrir archivo

mi_archivo.read() # leer archivo si lo imprimo muestra la informacion

mi_archivo.readline() # solo lee una linea al imprimir

mi_archivo.close() # siempre cerrar el archivo, para evitar consumo de memoria

print(mi_archivo)