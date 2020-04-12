import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# df_all_norm = pd.read_csv('/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/norm_5_days.csv')
df_all_norm = pd.read_csv('/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/all_without_11.csv')
print (df_all_norm)

df_mean = df_all_norm.groupby('color').mean()
print (df_mean)

df_mean.to_csv('mean_all_without_11.csv')