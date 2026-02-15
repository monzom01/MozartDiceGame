import pandas as pd
from music21 import converter, stream

def generar_vals_patron():
    df = pd.read_excel("Matriz_Mozart_Final.xlsx")
    obra = stream.Score()
    parte = stream.Part()
    
    # TU PATRÓN: 2, 4, 6
    patron = [2, 4, 6]
    
    print(f"--- Generando patrón matemático: {patron} ---")
    
    # 'i' será el número de compás (0, 1, 2)
    # 'suma' será el valor del dado (2, 4, 6)
    for i, suma in enumerate(patron):
        columna = f'Compas_{i+1}'
        
        # Esta línea es la que "extrae" el número del Excel
        fragmento_id = df.loc[df['Suma_Dados'] == suma, columna].values[0]
        
        archivo = f"midis/{fragmento_id}.mid"
        
        # Cargamos y añadimos a la partitura
        print(f"Compás {i+1}: Suma {suma} -> Archivo {fragmento_id}.mid")
        fragmento = converter.parse(archivo)
        
        # Lo metemos en un compás y a la parte
        compas = stream.Measure(number=i+1)
        for elemento in fragmento.flatten().notesAndRests:
            compas.insert(elemento.offset, elemento)
        parte.append(compas)

    obra.insert(0, parte)
    obra.write('midi', fp='Vals_Patron_246.mid')
    print("--- ¡Archivo Vals_Patron_246.mid creado! ---")

if __name__ == "__main__":
    generar_vals_patron()