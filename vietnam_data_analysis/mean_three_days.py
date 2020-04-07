import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_all_norm = pd.read_csv('three_days_norm.csv')
print (df_all_norm)

df_mean = df_all_norm.groupby('color').mean()
print (df_mean)

df_mean.to_csv('mean_norm_three_days.csv')