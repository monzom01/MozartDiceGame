import pandas as pd

# Datos reales de los primeros 8 compases (la primera mitad del Minueto)
# Estos números corresponden a los fragmentos originales de Mozart
data = {
    'Suma_Dados': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Compas_1': [96, 32, 69, 40, 148, 104, 152, 119, 98, 3, 54],
    'Compas_2': [22, 6, 95, 17, 74, 157, 60, 84, 142, 87, 130],
    'Compas_3': [141, 128, 158, 113, 163, 27, 171, 114, 42, 165, 10],
    'Compas_4': [41, 63, 13, 85, 45, 167, 53, 50, 156, 115, 103],
    'Compas_5': [105, 146, 153, 161, 80, 154, 99, 140, 75, 102, 28],
    'Compas_6': [122, 46, 55, 2, 97, 68, 133, 86, 129, 4, 37],
    'Compas_7': [11, 134, 110, 159, 36, 118, 21, 169, 62, 31, 106],
    'Compas_8': [30, 81, 24, 100, 107, 91, 127, 94, 123, 164, 5]
}

df = pd.DataFrame(data)
# Guardamos con un nombre claro
df.to_excel("Matriz_Mozart_8Compases.xlsx", index=False)
print("--- Paso 1 Completado: Se ha creado 'Matriz_Mozart_8Compases.xlsx' ---")