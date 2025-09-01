
# validador_simple.py
# -*- coding: utf-8 -*-
import os

def archivo_ok(ruta, minimo_bytes=1):
    return os.path.exists(ruta) and os.path.getsize(ruta) >= minimo_bytes

def main():
    archivos = [
        ("datos_in.txt", 1),
        ("datos_out.txt", 10),
        ("grafico_out.jpg", 100)
    ]

    problemas = []
    for ruta, minimo in archivos:
        if not archivo_ok(ruta, minimo):
            problemas.append(f"- {ruta} no existe o está vacío (< {minimo} bytes)")

    if problemas:
        print("Validación: FALLÓ")
        for p in problemas:
            print(p)
        print("Nota: 0")
    else:
        print("Validación: OK")
        print("Nota: 5")

if __name__ == "__main__":
    main()