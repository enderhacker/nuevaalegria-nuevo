# Damos bienvenida e importamos todo
print("Bienvenido a la app para elegir ejercicios de natacion")
import random


# Definir los objetivos y los archivos de entrenamiento correspondientes
objetivos = {
    "bajar peso": "ejercicios_bajar_peso.txt",
    "pasar el tiempo": "ejercicios_pasar_tiempo.txt",
    "entrenar": "ejercicios_entrenar.txt",
    "bucear": "ejercicios_bucear.txt"
}

# Preguntar objetivo en funcion de los disponibles
print("Elige un objetivo:")
for i, objetivo in enumerate(objetivos.keys()):
    print(f"{i+1}. {objetivo}")
opcion = int(input("Opción: "))

# Obtener la lista de ejercicios correspondiente al objetivo seleccionado
opcion_elegida = list(objetivos.keys())[opcion - 1]
archivo_ejercicios = objetivos[opcion_elegida]

# Leer el archivo de ejercicios y obtener una opción aleatoria
with open(archivo_ejercicios, "r") as file:
    ejercicios = file.readlines()
ejercicio_aleatorio = random.choice(ejercicios)

# Imprimir los resultados
print(f"\nPara el objetivo '{opcion_elegida}',")
print(f"se recomienda el siguiente ejercicio:\n")
print(ejercicio_aleatorio)