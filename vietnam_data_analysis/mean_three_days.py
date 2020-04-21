import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fname = '/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/analysis by days_sum_activites/5_days_norm_activities.csv'
# df_all_norm = pd.read_csv('/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/norm_5_days.csv')
# df_all_norm = pd.read_csv('/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/all_without_11.csv')
df = pd.read_csv(fname)
print (df)

df_mean = df.groupby('color').mean()
print (df_mean)

df_mean.to_csv('mean_5_days_norm_activities.csv')