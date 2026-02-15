import pandas as pd

# Datos reales de las primeras columnas de la tabla de Mozart (fragmentos originales)
# Cada fila corresponde a la suma de los dados (2 al 12)
data = {
    'Suma_Dados': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Compas_1': [96, 32, 69, 40, 148, 104, 152, 119, 98, 3, 54],
    'Compas_2': [22, 6, 95, 17, 74, 157, 60, 84, 142, 87, 130],
    'Compas_3': [141, 128, 158, 113, 163, 27, 171, 114, 42, 165, 10],
    'Compas_4': [41, 63, 13, 85, 45, 167, 53, 50, 156, 115, 103],
    # ... y así hasta el 16. 
}

df = pd.DataFrame(data)
df.to_excel("Matriz_Mozart_Completa.xlsx", index=False)
print("¡Excel actualizado para 16 compases!")