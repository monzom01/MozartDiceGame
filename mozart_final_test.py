import pandas as pd
import os
from music21 import converter, stream, meter

def buscar_archivo_midi(numero):
    posibles_nombres = [f"{numero}.mid", f"{numero}.MID", f"M{numero}.mid", f"M{numero}.MID"]
    for nombre in posibles_nombres:
        ruta = os.path.join("midis", nombre)
        if os.path.exists(ruta): return ruta
    return None

def generar_vals():
    df = pd.read_excel("Matriz_Mozart_Final.xlsx")
    
    # Usamos Stream básico, que es menos propenso a errores de "partitura vacía"
    contenedor_final = stream.Stream()
    
    # Tu patrón de prueba
    patron = [4, 3, 3, 5, 11, 11, 12, 12]
    
    print(f"--- Generando {len(patron)} compases ---")
    
    for i, suma in enumerate(patron):
        num_compas = i + 1
        columna = f'Compas_{num_compas}'
        
        id_midi = df.loc[df['Suma_Dados'] == suma, columna].values[0]
        ruta = buscar_archivo_midi(id_midi)
        
        if ruta:
            try:
                # Cargamos el fragmento y le quitamos metadatos raros con .flatten()
                fragmento = converter.parse(ruta).flatten()
                
                # Le asignamos el tiempo 3/4 por si acaso
                fragmento.insert(0, meter.TimeSignature('3/4'))
                
                # Lo pegamos al final de lo que ya llevamos
                contenedor_final.append(fragmento)
                print(f"Compás {num_compas}: {id_midi} cargado.")
            except Exception as e:
                print(f"Error en {id_midi}: {e}")

    # Escribimos el archivo de salida
    archivo_salida = 'Prueba_Final_Mozart.mid'
    
    # Forzamos la escritura sin procesamientos extraños
    contenedor_final.write('midi', fp=archivo_salida)
    print(f"\n--- ¡ARCHIVO CREADO!: {archivo_salida} ---")

if __name__ == "__main__":
    generar_vals()