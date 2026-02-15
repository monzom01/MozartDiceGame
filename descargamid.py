import urllib.request
import os

def descargar_seguro():
    if not os.path.exists('midis'):
        os.makedirs('midis')
    
    # Probamos una ruta que suele ser más estable
    base_url = "https://w3.cs.jmu.edu/bernstdh/web/common/help/mozart/midis/m"
    
    for i in range(1, 177):
        destino = f"midis/{i}.mid"
        if os.path.exists(destino): continue # Si ya lo bajó, se lo salta
        
        url = f"{base_url}{i}.mid"
        try:
            # timeout=5 evita que se quede colgado esperando
            with urllib.request.urlopen(url, timeout=5) as response, open(destino, 'wb') as out_file:
                out_file.write(response.read())
            print(f"OK: {i}.mid")
        except:
            print(f"Saltando {i} (no disponible)")

    print("--- Proceso finalizado ---")

if __name__ == "__main__":
    descargar_seguro()