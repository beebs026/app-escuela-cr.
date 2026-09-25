import json
import os

ARCHIVO = 'usuarios.json'

def guardar_usuario (datos_usuario):
        usuarios = cargar_usuarios()
        usuarios.append(datos_usuario)
        with open(ARCHIVO, 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
            
def cargar_usuarios():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, 'r', encoding='utf-8') as f:
        return json.load(f)