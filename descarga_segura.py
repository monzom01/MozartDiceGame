import requests
import os
import sys

def descargar():
    folder = 'midis'
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Probamos con una fuente alternativa muy estable
    base_url = "https://raw.githubusercontent.com/asprenger/mozart-dice-game/master/midi/m{}.mid"

    print("--- Presiona Ctrl+C en cualquier momento para DETENER ---")
    
    try:
        for i in range(1, 177):
            file_path = f"{folder}/{i}.mid"
            
            # Si el archivo ya existe, saltamos al siguiente
            if os.path.exists(file_path):
                continue

            url = base_url.format(i)
            try:
                # 'timeout=3' asegura que si no responde en 3 segundos, pase al siguiente
                r = requests.get(url, timeout=3)
                if r.status_code == 200:
                    with open(file_path, 'wb') as f:
                        f.write(r.content)
                    print(f"Descargado: {i}.mid")
                else:
                    print(f"No encontrado: {i}.mid (Error {r.status_code})")
            except requests.exceptions.RequestException:
                print(f"Error de conexión en archivo {i}, saltando...")

    except KeyboardInterrupt:
        print("\n\n--- DETENIDO POR EL USUARIO ---")
        sys.exit()

if __name__ == "__main__":
    descargar()