import pandas as pd

# Creamos una matriz simplificada (Suma de dados vs Compás)
data = {
    'Suma_Dados': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Compas_1': [96, 32, 69, 40, 148, 104, 152, 119, 98, 3, 54],
    'Compas_2': [22, 6, 95, 17, 74, 157, 60, 84, 142, 87, 130],
    'Compas_3': [141, 128, 158, 113, 163, 27, 171, 114, 42, 165, 10]
}

df = pd.DataFrame(data)
df.to_excel("Matriz_Mozart.xlsx", index=False)
print("¡Archivo Matriz_Mozart.xlsx creado con éxito!")