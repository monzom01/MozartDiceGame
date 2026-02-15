import pandas as pd
import os
from music21 import converter, stream, meter  # 1. Agregamos 'meter' aquí

def buscar_archivo_midi(numero):
    posibles_nombres = [f"{numero}.mid", f"{numero}.MID", f"M{numero}.mid", f"M{numero}.MID"]
    for nombre in posibles_nombres:
        ruta = os.path.join("midis", nombre)
        if os.path.exists(ruta):
            return ruta
    return None

def generar_vals_extremos():
    df = pd.read_excel("Matriz_Mozart_Final.xlsx")
    obra = stream.Score()
    parte = stream.Part()
    
    patron = [4, 3, 3, 5, 11, 11, 12, 12]
    print(f"--- Componiendo con patrón extremo: {patron} ---")
    
    for i, suma in enumerate(patron):
        num_compas = i + 1
        columna = f'Compas_{num_compas}'
        
        fragmento_id = df.loc[df['Suma_Dados'] == suma, columna].values[0]
        ruta_archivo = buscar_archivo_midi(fragmento_id)
        
        if ruta_archivo:
            try:
                fragmento = converter.parse(ruta_archivo)
                compas = stream.Measure(number=num_compas)
                
                # 2. CORRECCIÓN: Usamos meter.TimeSignature
                compas.timeSignature = meter.TimeSignature('3/4')
                
                for elemento in fragmento.flatten().notesAndRests:
                    if elemento.offset < 3.0:
                        compas.insert(elemento.offset, elemento)
                
                parte.append(compas)
                print(f"Compás {num_compas}: Suma {suma} -> Cargado {ruta_archivo}")
            except Exception as e:
                print(f"Error procesando {ruta_archivo}: {e}")
        else:
            print(f"¡ALERTA! No encontré el archivo {fragmento_id}")

    obra.insert(0, parte)
    obra.write('midi', fp='Vals_Extremos_Omar.mid')
    print("\n--- ¡AHORA SÍ! Archivo 'Vals_Extremos_Omar.mid' creado ---")

if __name__ == "__main__":
    generar_vals_extremos()