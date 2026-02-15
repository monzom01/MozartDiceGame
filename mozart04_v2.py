import pandas as pd
import os
from music21 import converter, stream, meter

# Asegúrate de que esta función esté en tu archivo también
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
    
    for i, suma in enumerate(patron):
        num_compas = i + 1
        columna = f'Compas_{num_compas}'
        fragmento_id = df.loc[df['Suma_Dados'] == suma, columna].values[0]
        ruta_archivo = buscar_archivo_midi(fragmento_id)
        
        if ruta_archivo:
            try:
                fragmento = converter.parse(ruta_archivo)
                compas = stream.Measure(number=num_compas)
                compas.timeSignature = meter.TimeSignature('3/4')
                
                # Aquí está lo que comentaste, ahora bien estructurado
                for el in fragmento.flatten().notesAndRests:
                    compas.insert(el.offset, el)
                
                parte.append(compas)
                print(f"Compás {num_compas}: Cargado con éxito")
            except Exception as e:
                print(f"Error en compás {num_compas}: {e}")

    obra.append(parte)
    
    # Generamos el archivo
    nombre_archivo = 'Vals_Extremos_v2.mid'
    obra.write('midi', fp=nombre_archivo)
    print(f"\n--- ¡ÉXITO! Archivo '{nombre_archivo}' generado ---")

# ¡ESTO ES LO QUE FALTABA! El disparador.
if __name__ == "__main__":
    generar_vals_extremos()