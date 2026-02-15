import pandas as pd
from music21 import converter, stream

def generar_vals_personalizado():
    # 1. Ingrediente: El Mapa
    df = pd.read_excel("Matriz_Mozart_Final.xlsx")
    obra = stream.Score()
    parte = stream.Part()
    
    # 2. Ingrediente: TUS DADOS (Aquí están tus números)
    mis_dados = [3, 6, 9, 11] # Cambié el 1 por 11 para que sea válido
    
    print(f"--- Componiendo el Vals de Omar con los números: {mis_dados} ---")
    
    # 3. La lógica: Recorremos tus números uno por uno
    # 'enumerate' nos da el índice (0, 1, 2...) y el valor (3, 6, 9...)
    for i, valor_dado in enumerate(mis_dados):
        numero_compas = i + 1
        
        # Buscamos en el Excel usando tu número de dado
        fragmento_id = df.loc[df['Suma_Dados'] == valor_dado, f'Compas_{numero_compas}'].values[0]
        
        archivo = f"midis/{fragmento_id}.mid"
        try:
            fragmento = converter.parse(archivo)
            # Limpiamos y metemos en un compas
            compas = stream.Measure(number=numero_compas)
            for elemento in fragmento.flatten().notesAndRests:
                compas.insert(elemento.offset, elemento)
            
            parte.append(compas)
            print(f"Compás {numero_compas}: Dado {valor_dado} -> Usando {fragmento_id}.mid")
        except:
            print(f"Error con el archivo {archivo}")

    obra.insert(0, parte)
    # 4. El Resultado
    nombre_salida = "Vals_Omar_Personalizado.mid"
    obra.write('midi', fp=nombre_salida)
    print(f"--- ¡Listo! Creado: {nombre_salida} ---")

if __name__ == "__main__":
    generar_vals_personalizado()