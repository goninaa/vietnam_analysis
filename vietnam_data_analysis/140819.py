import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def norm(df_all):
    df_all_norm = df_all.copy()
    df_all_norm.drop(['location'],axis = 1, inplace = True)
    for col in df_all_norm.columns[2:]:
        df_all_norm[col] = df_all[col]/df_all['sum'] 

    df_all_norm = df_all_norm[['file', 'color', 'search', 'approach', 'buzz1', 'buzz2', 'attack','sum buzz+attack', 'sum']]
    return df_all_norm
    
def save_file(df_all_norm, trail_day):
    df_all_norm.to_csv(f'{trail_day}_df_norm.csv')


df_all = pd.read_csv('140819.csv')
# print (df_all.head())
df_all.replace({'white':1,'black':0}, inplace = True)
print (df_all.head())
df_all_norm = norm(df_all)
print (df_all_norm)

df_all_norm.drop([0], axis = 0, inplace = True)
# print (df_all_norm.iloc[0])
print (df_all_norm)
save_file(df_all_norm, '140819_without11')