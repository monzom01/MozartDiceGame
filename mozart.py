import random

# Esto es una versión simplificada de la tabla de Mozart (solo 3 compases)
# En un script completo, aquí irían los 176 fragmentos reales.
tabla_mozart = {
    2:  [96, 22, 141],
    3:  [32, 6, 128],
    7:  [176, 2, 104], # Fila del 7 que usamos en el ejemplo
    12: [142, 55, 20]
}

def componer_minueto():
    minueto = []
    for compas_num in range(3): # Generamos 3 compases
        suma_dados = random.randint(1, 6) + random.randint(1, 6)
        # Si la suma no está en nuestra tabla simplificada, usamos el 7 por defecto
        fragmento = tabla_mozart.get(suma_dados, tabla_mozart[7])[compas_num]
        minueto.append(fragmento)
    return minueto

resultado = componer_minueto()
print(f"Tu composición de Mozart es la secuencia de fragmentos: {resultado}")

