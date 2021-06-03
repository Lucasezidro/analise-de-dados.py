import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

arquivo_excel_1 = '1e2.xlsx'
arquivo_excel_2 = '3.xlsx'

df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name='dia1')
df_dia_2 = pd.read_excel(arquivo_excel_1, sheet_name='dia2')
df_dia_3 = pd.read_excel(arquivo_excel_2)

df_todas = pd.concat([df_dia_1, df_dia_2, df_dia3])

# print(df_todas)['vendedor']

lucro = df_todas.groupby(['vendedor']).sum()
# print(lucro)

relatorio = lucro.loc[:,'unidade':'preco']

relatorio.plot(kind='bar')
plt.show()
