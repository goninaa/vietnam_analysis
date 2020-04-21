import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import friedmanchisquare

# df_all_norm = pd.read_csv('three_days_norm.csv')
df_all_norm = pd.read_csv('/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/norm_5_days.csv')
# print (df_all_norm.tail())
df_11 = df_all_norm.loc[df_all_norm['date']=='11/08/2019']
df_13 = df_all_norm.loc[df_all_norm['date']=='13/08/2019']
df_14 = df_all_norm.loc[df_all_norm['date']=='14/08/2019']
df_17 = df_all_norm.loc[df_all_norm['date']=='17/08/2019']
df_18 = df_all_norm.loc[df_all_norm['date']=='18/08/2019']


# def correl_df (df, title, fname):
#     # cols = df_all_norm.columns
#     cols = ['color', 'search','approach','buzz1','buzz2', 'attack', 'sum buzz+attack']
#     cm = np.corrcoef(df[cols].values.T)
#     #sns.set(font_scale=1.5)
#     hm = sns.heatmap(cm,
#                     cbar=True,
#                     annot=True,
#                     square=True,
#                     fmt='.2f',
#                     annot_kws={'size': 9},
#                     yticklabels=cols,
#                     xticklabels=cols)

#     plt.title (title)
#     plt.tight_layout()
#     # plt.savefig(f'{df.date[0]}.png', dpi=300)
#     plt.savefig(f'{fname}_correl.png', dpi=300)
#     plt.show()

# # correl_df(df_11,'11/08/19' ,'df_11')
# # correl_df(df_13, '13/08/19', 'df_13')
# # correl_df(df_14, '14/08/19', 'df_14')
# # correl_df(df_all_norm, 'Three days', 'df_all_norm')

# # def t_test(df, title, name):
# def t_test(df, night):
#     t_dict = {}
#     df_t = pd.DataFrame()
#     white = df[df['color'] == 1]
#     black = df[df['color'] == 0]
#     cols = ['search','approach','buzz1','buzz2', 'attack', 'sum buzz+attack']
#     for col in cols:
#         t_stat = ttest_ind(white[col],black[col])
#         t_dict[col] = t_stat
#     df_t = pd.DataFrame.from_dict(t_dict)
#     df_t.index = ('stat', 'pvalue')
#     df_t.to_csv(f'df_t_{night}.csv')
#     return t_dict, df_t

   
# t_dict_11, df_t_11 = t_test(df_11, 11)
# t_dict_13, df_t_13 = t_test(df_13, 13)
# t_dict_14, df_t_14 = t_test(df_14, 14)
# t_dict_17, df_t_17 = t_test(df_17, 17)
# t_dict_18, df_t_18 = t_test(df_18, 18)
# t_dict_all, df_t_all = t_test(df_all_norm, 'all')

# # t_dict_all_no_11, df_t_all_no_11 = t_test(df_all_no_11, 'all_without_11')
# print (df_t_13)
# print (df_t_14)
# print (df_t_all)

# # def box_plot (df, col, fname):
# # def box_plot (df, fname):
# #     cols = ['search','approach','buzz1','buzz2', 'attack', 'sum buzz+attack']
# #     # boxplot = df.boxplot(column=cols, by=['color'], layout=(2, 3))
# #     # fig, ax = plt.subplots(2, 3, figsize=(10, 5))
# #     plt.subplots(2, 3, figsize=(10, 5))
# #     for col in cols:
# #         df.boxplot(column=col, by=['color'])
# #     # data.boxplot('BOD','Group', ax=ax[1])
# #     plt.tight_layout()
# #     plt.suptitle(f'{fname}', y=1.08)
# #     # plt.savefig(f'{fname}_boxplot.png', dpi=300)
# #     plt.show()

# def box_plot (df, col, fname):
    
#     boxplot = df.boxplot(column=col, by=['color'])
#     plt.tight_layout()
#     plt.suptitle(f'{fname}', y=1.08)
#     plt.savefig(f'{fname}_{col}boxplot.png', dpi=300, bbox_inches="tight")
#     plt.show()

# # def friedman_test(df, col, fname):
# #     """Friedman test"""
# #     # compare samples
# #     stat, p = friedmanchisquare(data1, data2, data3)
# #     print('Statistics=%.3f, p=%.3f' % (stat, p))
# #     # interpret
# #     alpha = 0.05
# #     if p > alpha:
# #         print('Same distributions (fail to reject H0)')
# #     else:
# #         print('Different distributions (reject H0)')


# # b = box_plot(df_11,'11.8.19')

# cols = ['search','approach','buzz1','buzz2', 'attack', 'sum buzz+attack']
# # plt.subplots(2, 3)
# # for i in range(2):
# #     for j in range(3):
# #        box_plot(df_11, cols[i] ,'11.8.19')
#     # box_plot(df_11, cols[i] ,'11.8.19')

# for col in cols:
#     b = box_plot(df_11, col ,'11.8.19')

# for col in cols:
#     b = box_plot(df_13, col ,'13.8.19')

# for col in cols:
#     b = box_plot(df_14, col ,'14.8.19')

# for col in cols:
#     b = box_plot(df_17, col ,'17.8.19')

# for col in cols:
#     b = box_plot(df_18, col ,'18.8.19')

# for col in cols:
#     b = box_plot(df_all_norm, col ,'all nights')

# # for col in cols:
# #     b = box_plot(df_all_no_11, col ,'all nights')

# # for col in cols:
# #     b = box_plot(df_all_norm, col ,'Three days')


#     """Friedman test"""

# print (df_11.iloc[0][3:])
data1 = df_11.iloc[0][5]
data2 = df_11.iloc[1][5]
data3 = df_11.iloc[2][5]
#     # compare samples
# data1, data2, data3 = df_11 
stat, p = friedmanchisquare(data1, data2, data3)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distributions (fail to reject H0)')
else:
    print('Different distributions (reject H0)')