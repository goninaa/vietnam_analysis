import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# df_all_norm = pd.read_csv('three_days_norm.csv')
df_all = pd.read_csv('/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/all_days_24_devices_not_normalized/all_days_24_devices.csv')
# df_all_norm = pd.read_csv('/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/analysis by strings/string1.csv')
# print (df_all_norm.tail())
# df_11 = df_all_norm.loc[df_all_norm['date']=='11/08/2019']
# df_13 = df_all_norm.loc[df_all_norm['date']=='13/08/2019']
# df_14 = df_all_norm.loc[df_all_norm['date']=='14/08/2019']
# df_17 = df_all_norm.loc[df_all_norm['date']=='17/08/2019']
# df_18 = df_all_norm.loc[df_all_norm['date']=='18/08/2019']
df_11 = df_all.loc[df_all['date']=='11/08/2019']
df_13 = df_all.loc[df_all['date']=='13/08/2019']
df_14 = df_all.loc[df_all['date']=='14/08/2019']
df_17 = df_all.loc[df_all['date']=='17/08/2019']
df_18 = df_all.loc[df_all['date']=='18/08/2019']
# df_a = df_all_norm.loc[df_all_norm['location']=='a']
# df_b = df_all_norm.loc[df_all_norm['location']=='b']
# df_c = df_all_norm.loc[df_all_norm['location']=='c']
# df_d = df_all_norm.loc[df_all_norm['location']=='d']
# df_e = df_all_norm.loc[df_all_norm['location']=='e']
# df_f = df_all_norm.loc[df_all_norm['location']=='f']
# df_2 = df_all_norm.loc[df_all_norm['string location']==2]
# df_3 = df_all_norm.loc[df_all_norm['string location']==3]
# df_close = pd.concat([df_a, df_c, df_e])
# df_far = pd.concat([df_b, df_d,df_f])
print (df_all)


# def t_test(df, night):
#     t_dict = {}
#     df_t = pd.DataFrame()
#     # white = df[df['color'] == 1]
#     # black = df[df['color'] == 0]
#     df_11 = df.loc[df['date']=='11/08/2019']
#     df_13 = df.loc[df['date']=='13/08/2019']
#     df_14 = df.loc[df['date']=='14/08/2019']
#     df_17 = df.loc[df['date']=='17/08/2019']
#     df_18 = df.loc[df['date']=='18/08/2019']
#     # cols = ['sum buzzes','sum buzz+attack','sum activities']
#     # cols = ['search','approach','buzz1','buzz2', 'attack', 'sum buzz+attack', 'sum', 'sum buzzes','sum activities','search-approach']
#     dates = [df_11,df_13,df_14,df_17,df_18]
#     cols = ['sum']
#     for date in dates:
#         t_stat = ttest_ind(date[cols],df_11[cols])
#         print (t_stat)
#         t_dict[date] = t_stat
#     df_t = pd.DataFrame.from_dict(t_dict)
#     df_t.index = ('stat', 'pvalue')
#     # df_t.to_csv(f'df_t_{date}.csv')
#     print (df_t)
#     return t_dict, df_t

    # for col in cols:
    #     # t_stat = ttest_ind(white[col],black[col])
    #     # t_stat = ttest_ind(df_11[col],df_13[col],df_14[col],df_17[col],df_18[col])
    #     t_stat = ttest_ind(df_11[col],df_13[col])
    #     t_dict[col] = t_stat
    # df_t = pd.DataFrame.from_dict(t_dict)
    # df_t.index = ('stat', 'pvalue')
    # df_t.to_csv(f'df_t_{night}.csv')
    # print (df_t)
    # return t_dict, df_t

   
# t_dict_11, df_t_11 = t_test(df_11, 11)
# t_dict_13, df_t_13 = t_test(df_13, 13)
# t_dict_14, df_t_14 = t_test(df_14, 14)
# t_dict_17, df_t_17 = t_test(df_17, 17)
# t_dict_18, df_t_18 = t_test(df_18, 18)
# t_dict_1, df_t_1 = t_test(df_1, 'string1')
# t_dict_close, df_t_close = t_test(df_close, 'loc_close')
# t_dict_far, df_t_far = t_test(df_far, 'loc_far')
# t_dict_3, df_t_3 = t_test(df_3, 'string3')
# t_dict_all, df_t_all = t_test(df_all_norm, 'all')
# t_dict_all, df_t_all = t_test(df_all, 'all')

# t_dict_all_no_11, df_t_all_no_11 = t_test(df_all_no_11, 'all_without_11')
# print (df_t_13)
# print (df_t_14)
# print (df_t_all)

# def box_plot (df, col, fname):
# def box_plot (df, fname):
#     cols = ['search','approach','buzz1','buzz2', 'attack', 'sum buzz+attack']
#     # boxplot = df.boxplot(column=cols, by=['color'], layout=(2, 3))
#     # fig, ax = plt.subplots(2, 3, figsize=(10, 5))
#     plt.subplots(2, 3, figsize=(10, 5))
#     for col in cols:
#         df.boxplot(column=col, by=['color'])
#     # data.boxplot('BOD','Group', ax=ax[1])
#     plt.tight_layout()
#     plt.suptitle(f'{fname}', y=1.08)
#     # plt.savefig(f'{fname}_boxplot.png', dpi=300)
#     plt.show()

def box_plot (df, col, fname):
    
    boxplot = df.boxplot(column=col, by=['date'])
    plt.tight_layout()
    plt.suptitle(f'{fname}', y=1.08)
    plt.savefig(f'{fname}_{col}boxplot.png', dpi=300, bbox_inches="tight")
    plt.show()


# b = box_plot(df_11,'11.8.19')
# cols = ['sum buzzes','sum buzz+attack','sum activities']
cols = ['search','approach','buzz1','buzz2', 'attack', 'sum buzz+attack', 'sum']
# cols = ['search','approach','buzz1','buzz2', 'attack', 'sum buzz+attack', 'sum', 'sum buzzes','sum activities','search-approach']
# cols = ['sum']
# plt.subplots(2, 3)
# for i in range(2):
#     for j in range(3):
#        box_plot(df_11, cols[i] ,'11.8.19')
    # box_plot(df_11, cols[i] ,'11.8.19')

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
    # b = box_plot(df_all_norm, col ,'all nights')

# for col in cols:
#     b = box_plot(df_all, col ,'all nights')

# for col in cols:
#     b = box_plot(df_1, col ,'string 1')

# for col in cols:
#     b = box_plot(df_2, col ,'string 2')

# for col in cols:
#     b = box_plot(df_close, col ,'loc_close')

# for col in cols:
#     b = box_plot(df_far, col ,'loc_far')