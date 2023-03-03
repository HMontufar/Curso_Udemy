import os, re, time, math, datetime
from pathlib import Path


inicio = time.time()


# Accediendo a la ruta de carpetas y archivos para la busqueda de información

route = 'D:\\Datos_Perfil\\507266\\Desktop\\Python_HMG\\buscador_no_serie\\Mi_Gran_Directorio'


# Creando variables y patron de busqueda

mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []


# Funciones 

def buscar_numero(archivos, patron):
    este_archivo = open(archivos, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpetas, subcarpetas, archivo in os.walk(route):
        for a in archivo:
            resultado = buscar_numero(Path(carpetas, a), mi_patron)
            if resultado != '':
                numeros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNUM. SERIE')
    print('-------\t\t\t----------')
    
    for a in archivos_encontrados:
        print(f'{a}\t{numeros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros encontrados: {len(numeros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()