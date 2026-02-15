import pandas as pd
import random
from music21 import converter, stream, stream # Agregamos stream aquí

def generar_minueto_completo():
    df = pd.read_excel("Matriz_Mozart_Final.xlsx")
    obra = stream.Score() # Cambiamos Stream por Score (Partitura)
    parte = stream.Part() # Creamos una parte musical
    
    print("--- Componiendo Minueto de 16 compases ---")
    
    for i in range(1, 17):
        dados = random.randint(1, 6) + random.randint(1, 6)
        fragmento_id = df.loc[df['Suma_Dados'] == dados, f'Compas_{i}'].values[0]
        
        archivo = f"midis/{fragmento_id}.mid"
        try:
            # CARGAMOS EL FRAGMENTO
            fragmento = converter.parse(archivo)
            
            # SOLUCIÓN: Metemos el fragmento dentro de un objeto 'Measure' (Compás)
            compas_contenedor = stream.Measure(number=i)
            for elemento in fragmento.flatten().notesAndRests:
                compas_contenedor.insert(elemento.offset, elemento)
            
            parte.append(compas_contenedor)
            print(f"Compás {i}: Dados {dados} -> Usando {archivo}")
        except Exception as e:
            print(f"Ojo: No pude procesar el archivo {archivo}. Error: {e}")

    obra.insert(0, parte)
    # Guardamos el archivo final
    obra.write('midi', fp='Mi_Primer_Mozart.mid')
    print("\n--- ¡ÉXITO TOTAL! Archivo 'Mi_Primer_Mozart.mid' creado ---")

if __name__ == "__main__":
    generar_minueto_completo()