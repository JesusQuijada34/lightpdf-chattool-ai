import os

archivo = "archivo.word"
if not os.path.exists(archivo):
    print(f"\033[31m🚫 El archivo no existe: {archivo}\033[0m")
else:
    tarea_id = crear_tarea_embedding(archivo)
    if tarea_id:
        obtener_resultado_embedding(tarea_id)

