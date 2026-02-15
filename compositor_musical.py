import pandas as pd
import random
from music21 import stream, note, chord, midi

def generar_musica():
    # 1. Leer la matriz desde Excel
    df = pd.read_excel("Matriz_Mozart.xlsx")
    
    score = stream.Score()
    part = stream.Part()
    
    print("Componiendo...")
    
    # 2. Simular los dados para 3 compases
    for i in range(1, 4):
        suma = random.randint(1, 6) + random.randint(1, 6)
        # Buscamos el fragmento en el Excel según la suma
        fila = df[df['Suma_Dados'] == suma]
        fragmento_id = fila[f'Compas_{i}'].values[0]
        
        print(f"Compás {i}: Dados sumaron {suma} -> Usando fragmento #{fragmento_id}")
        
        # 3. Mapeo simbólico (Aquí simplificamos notas para el ejemplo)
        # En el juego real, cada ID corresponde a una melodía grabada.
        n = note.Note("C4")
        if fragmento_id % 2 == 0: n = note.Note("E4")
        if fragmento_id % 3 == 0: n = note.Note("G4")
        
        n.quarterLength = 4.0 # Duración de un compás de 4/4
        part.append(n)

    score.append(part)
    
    # 4. Guardar como archivo de sonido MIDI
    mf = midi.translate.streamToMidiFile(score)
    mf.open("Mi_Composicion_Mozart.mid", 'wb')
    mf.write()
    mf.close()
    print("¡Listo! Escucha 'Mi_Composicion_Mozart.mid' en tu carpeta.")

if __name__ == "__main__":
    generar_musica()