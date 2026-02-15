import pandas as pd
import os
from music21 import converter, stream, meter

# ==========================================
#      ZONA DE PRUEBAS - MODIFICA AQUÍ
# ==========================================
# 1. Pon aquí los números de tus dados (de 2 al 12)
# Puedes poner la cantidad que quieras (ej: 4, 8 o 16 compases)
MIS_DADOS = [7, 7, 11, 2, 5, 8, 12, 3] 

# 2. Nombre del archivo de salida
NOMBRE_ARCHIVO = "Mi_Vals_Experimental_01.mid"
# ==========================================

def buscar_archivo_midi(numero):
    posibles_nombres = [f"{numero}.mid", f"{numero}.MID", f"M{numero}.mid", f"M{numero}.MID"]
    for nombre in posibles_nombres:
        ruta = os.path.join("midis", nombre)
        if os.path.exists(ruta): return ruta
    return None

def generar_musica():
    df = pd.read_excel("Matriz_Mozart_Final.xlsx")
    obra = stream.Score()
    parte = stream.Part()
    
    print(f"--- Generando {len(MIS_DADOS)} compases con el patrón {MIS_DADOS} ---")
    
    for i, suma in enumerate(MIS_DADOS):
        num_compas = i + 1
        # El juego original tiene 16 columnas. Si pides más de 16, 
        # volvemos a empezar desde la columna 1 (esto se llama 'módulo')
        col_index = ((num_compas - 1) % 16) + 1
        columna = f'Compas_{col_index}'
        
        try:
            fragmento_id = df.loc[df['Suma_Dados'] == suma, columna].values[0]
            ruta = buscar_archivo_midi(fragmento_id)
            
            if ruta:
                fragmento = converter.parse(ruta)
                compas = stream.Measure(number=num_compas)
                compas.timeSignature = meter.TimeSignature('3/4')
                
                # Insertamos las notas
                for el in fragmento.flatten().notesAndRests:
                    compas.insert(el.offset, el)
                
                parte.append(compas)
                print(f"Compás {num_compas}: OK (Basado en dado {suma})")
        except Exception as e:
            print(f"Error en compás {num_compas}: {e}")

    obra.append(parte)
    obra.write('midi', fp=NOMBRE_ARCHIVO)
    print(f"\n¡LISTO! Se ha creado: {NOMBRE_ARCHIVO}")

if __name__ == "__main__":
    generar_musica()