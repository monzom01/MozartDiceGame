import pandas as pd
import os
from music21 import converter, stream, meter

def buscar_archivo_midi(numero):
    posibles_nombres = [f"{numero}.mid", f"{numero}.MID", f"M{numero}.mid", f"M{numero}.MID"]
    for nombre in posibles_nombres:
        ruta = os.path.join("midis", nombre)
        if os.path.exists(ruta): return ruta
    return None

def generar_vals_profesional():
    df = pd.read_excel("Matriz_Mozart_Final.xlsx")
    obra = stream.Score()
    parte = stream.Part()
    
    # Probemos con tu patrón de 8 compases
    patron = [4, 3, 3, 5, 11, 11, 12, 12] 
    
    print("--- Iniciando generación limpia (sin silencios extra) ---")
    
    for i, suma in enumerate(patron):
        num_compas = i + 1
        col_index = ((num_compas - 1) % 16) + 1
        columna = f'Compas_{col_index}'
        
        fragmento_id = df.loc[df['Suma_Dados'] == suma, columna].values[0]
        ruta = buscar_archivo_midi(fragmento_id)
        
        if ruta:
            try:
                fragmento = converter.parse(ruta)
                compas = stream.Measure(number=num_compas)
                compas.timeSignature = meter.TimeSignature('3/4')
                
                # --- TÉCNICA ANTI-SILENCIO ---
                notas = fragmento.flatten().notesAndRests
                if len(notas) > 0:
                    # 1. Encontramos el "hueco" inicial del archivo original
                    desfase_inicial = notas[0].offset 
                    
                    for el in notas:
                        # 2. Restamos ese hueco para que la primera nota sea el tiempo 0
                        posicion_corregida = el.offset - desfase_inicial
                        
                        # 3. Solo lo dejamos pasar si está dentro de los 3 tiempos
                        if posicion_corregida < 3.0:
                            # Ajustamos también la duración si la nota es muy larga
                            if posicion_corregida + el.quarterLength > 3.0:
                                el.quarterLength = 3.0 - posicion_corregida
                            
                            compas.insert(posicion_corregida, el)
                
                parte.append(compas)
                print(f"Compás {num_compas}: Procesado y alineado.")
            except Exception as e:
                print(f"Error en compás {num_compas}: {e}")

    obra.append(parte)
    
    # Esto "llena" los huecos internos con silencios correctos para MuseScore
    obra.makeNotation(inPlace=True)
    
    output = 'Vals_Mozart_Limpio.mid'
    obra.write('midi', fp=output)
    print(f"\n--- ¡LISTO! Archivo generado: {output} ---")

if __name__ == "__main__":
    generar_vals_profesional()