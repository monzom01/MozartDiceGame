import urllib.request
import os

def descargar_musica():
    # Creamos la carpeta si no existe
    if not os.path.exists('midis'):
        os.makedirs('midis')
    
    # Esta es una fuente académica muy confiable (Universidad James Madison)
    base_url = "https://w3.cs.jmu.edu/bernstdh/web/common/help/mozart/midis/m"
    
    print("--- Iniciando descarga de los 176 fragmentos de Mozart ---")
    
    for i in range(1, 177):
        # El formato en esta web es m1.mid, m2.mid...
        file_name = f"m{i}.mid"
        url = base_url + str(i) + ".mid"
        
        # Destino final (solo el número para que tu otro script lo entienda)
        destino = f"midis/{i}.mid"
        
        try:
            urllib.request.urlretrieve(url, destino)
            if i % 20 == 0:
                print(f"Descargados {i} de 176...")
        except:
            print(f"Error en el fragmento {i}. Reintentando con otro formato...")
            # Plan B de nombre por si falla el primero
            try:
                url_alt = f"https://w3.cs.jmu.edu/bernstdh/web/common/help/mozart/midis/{i}.mid"
                urllib.request.urlretrieve(url_alt, destino)
            except:
                print(f"No se pudo descargar el {i}")

    print("--- ¡PROCESO TERMINADO! Revisa tu carpeta 'midis' ---")

if __name__ == "__main__":
    descargar_musica()