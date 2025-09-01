
# procesador_bar.py
# -*- coding: utf-8 -*-
"""
Clase sencilla para estudiantes de 1er semestre (sin pandas).
Pasos:
  1) Lee "datos_in.txt" con: n cc_uno cc_dos
  2) Genera n datos (b y c) usando semillas cc_uno y cc_dos, guarda "datos_out.txt"
  3) Lee "datos_out.txt", agrega columna aleatoria "etiqueta" y genera "grafico_out.jpg"
     mostrando cuántos hay de cada etiqueta en gráfico de barras.
"""
import os
import math
import random
import matplotlib.pyplot as plt
from collections import Counter

class ProcesadorDatos:
    def __init__(self, ruta_in="datos_in.txt", ruta_out="datos_out.txt", ruta_img="grafico_out.jpg"):
        self.ruta_in = ruta_in
        self.ruta_out = ruta_out
        self.ruta_img = ruta_img

        # Variables a llenar desde el archivo de entrada
        self.n = None
        self.cc_uno = None
        self.cc_dos = None

        # Categorías para el paso 3
        self.categorias = ["anciano","anciana","mujer","hombre","niño","niña"]

    # 1) Leer archivo de entrada
    def leer_datos_entrada(self):
        if not os.path.exists(self.ruta_in):
            raise FileNotFoundError("No se encontró el archivo: " + self.ruta_in)

        with open(self.ruta_in, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

        partes = contenido.split()
        if len(partes) < 3:
            raise ValueError("El archivo debe tener 3 valores: n cc_uno cc_dos")

        try:
            self.n = int(partes[0])
            self.cc_uno = int(partes[1])
            self.cc_dos = int(partes[2])
        except ValueError:
            raise ValueError("Los valores n, cc_uno y cc_dos deben ser enteros")

        print("n =", self.n)
        print("cc_uno =", self.cc_uno)
        print("cc_dos =", self.cc_dos)
        return "ok"

    # 2) Generar datos y guardarlos
    def generar_datos(self):
        if self.n is None or self.cc_uno is None or self.cc_dos is None:
            raise RuntimeError("Primero ejecute leer_datos_entrada()")

        rng_b = random.Random(self.cc_uno)
        rng_c = random.Random(self.cc_dos)
        with open("datos_out.txt", "w") as f:
            f.write("i,b,c\n")
            for i in range(1, self.n + 1):
                b = rng_b.uniform(-5, 5)  # valores aleatorios entre -5 y 5
                c = rng_c.uniform(0, 5)   # valores aleatorios entre 0 y 5
                f.write(f"{i},{b:.6f},{c:.6f}\n")
    
        return "ok"

    # 3) Leer datos_out, agregar etiqueta y graficar
    def leer_y_graficar(self):
        if not os.path.exists(self.ruta_out):
            raise FileNotFoundError("No se encontró el archivo: " + self.ruta_out)

        # Leemos manualmente el CSV
        with open(self.ruta_out, "r", encoding="utf-8") as f:
            lineas = f.read().strip().splitlines()

        if not lineas or not lineas[0].startswith("i,b,c"):
            raise ValueError("El archivo no tiene el encabezado esperado 'i,b,c'")
        etiquetas_posibles = ["anciano", "anciana", "mujer", "hombre", "niño", "niña"]

        etiquetas_asignadas = []

        for linea in lineas[1:]:
            partes = linea.split(",")
            if len(partes) != 3:
                continue
            etiqueta = random.choice(etiquetas_posibles)
            etiquetas_asignadas.append(etiqueta)

        # Contar frecuencia de cada etiqueta
        conteo = Counter(etiquetas_asignadas)

        # Gráfico de barras
        etiquetas = list(conteo.keys())
        cantidades = list(conteo.values())
        colores = {
            "anciano": "blue",
            "anciana": "purple",
            "mujer": "red",
            "hombre": "green",
            "niño": "orange",
            "niña": "pink"
        }

        plt.figure(figsize=(8, 6))
        plt.bar(etiquetas, cantidades, color=[colores[e] for e in etiquetas])
        plt.title("Cantidad de registros por etiqueta")
        plt.xlabel("Etiqueta")
        plt.ylabel("Cantidad")
        plt.grid(axis="y")
        plt.tight_layout()
        plt.savefig("grafico_out.jpg")
        plt.close()
        
        return "ok"


if __name__ == "__main__":
    proc = ProcesadorDatos()
    print("Paso 1:", proc.leer_datos_entrada())
    print("Paso 2:", proc.generar_datos())
    print("Paso 3:", proc.leer_y_graficar())