from django.shortcuts import render

# Create your views here.
import sqlite3

def buscar_usuario(nombre_usuario):
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()

    # ¡Vulnerabilidad! No se realiza la sanitización de la entrada del usuario.
    cursor.execute("SELECT * FROM usuarios WHERE nombre = '" + nombre_usuario + "'")

    usuario = cursor.fetchone()

    conexion.close()

    return usuario
