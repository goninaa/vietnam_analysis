import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DATA:
    """data from one file """
    def __init__(self, fname, color): #color: 1 white, 0 black
        self.fname = fname
        self.color = color
        # self.df = pd.DataFrame()
        self.df = pd.read_csv(self.fname)
        self.df_activity = pd.DataFrame()

    def add_color (self):
        self.df_activity['color'] = self.color
            
    def time_to_index (self): # need to be fixed in order to use
            """change time column into datetime index"""
            self.df.index = pd.to_datetime(self.df['time'])
            self.df.drop(['time'], axis=1, inplace=True)

    def count_activity (self):
        """ """
        self.df_activity = pd.DataFrame(self.df.copy().groupby('activity').count())
        self.df_activity = pd.DataFrame(self.df_activity['time'])
        self.df_activity.rename(columns={"time": f"{self.fname}"}, inplace = True)
        self.df_activity = self.df_activity.transpose()
        # self.df_activity = pd.Series(self.df_activity, name = self.fname)
    
    def run (self):
        self.count_activity()
        self.add_color()
        
       


if __name__ == "__main__":
    path = '/Users/gonina/Dropbox/vietnam-backup/mytois pilosus/excel analysis/devices_for_analysis/110819/'
    data1 = DATA(f'{path}Data_Frame_10.csv', 1)
    data2 = DATA(f'{path}Data_Frame_22.csv', 0)
    data3 = DATA(f'{path}Data_Frame_29.csv', 0)
    data4 = DATA(f'{path}Data_Frame_37.csv', 1)
    data5 = DATA(f'{path}Data_Frame_40.csv', 1)
    data6 = DATA(f'{path}Data_Frame_42.csv', 0)

    # data1 = DATA('Data_Frame_1.csv', 1)
    # data2 = DATA('Data_Frame_18.csv', 0)
    # data3 = DATA('Data_Frame_21.csv', 0)
    # data4 = DATA('Data_Frame_35.csv', 0)
    # data5 = DATA('Data_Frame_41.csv', 1)

    

    file_list = [data1,data2,data3,data4,data5,data6]
    all_data = []
    for f in file_list:
        f.run()
        all_data.append(f.df_activity)
    # print (all_data)

    # data1.run()
    # data2.run()
    # print (data1.df_activity)
    # print (data2.df_activity)

    # all_data = list([data1.df_activity, data2.df_activity])

    basic_df = all_data.pop(0)
    for df in all_data:
        basic_df = pd.concat([basic_df, df], sort = False)
    df_all = basic_df
    print (df_all)

    df_all = df_all.fillna(0)
    df_all['attack'] = df_all['attack']+ df_all['attack?']
    df_all.drop(['attack?'],axis = 1, inplace = True)
    # df_all['social call'] = df_all['social call']+ df_all['social calls']
    # df_all.drop(['social calls'],axis = 1, inplace = True)
    # df_all['sum'] = df_all.sum(axis=1)
    # df_all = df_all[['search', 'approach', 'buzz1', 'buzz2', 'attack','social call','empty', 'sum']]

    df_all.drop(['social calls', 'social call', 'empty'],axis = 1, inplace = True)
    # df_all['sum'] = df_all.sum(axis=1)
    df_all['sum'] = df_all['search']+ df_all['approach']+df_all['buzz1']+df_all['buzz2']+df_all['attack']
    df_all['sum buzz+attack'] = df_all['buzz1']+df_all['buzz2']+df_all['attack']
    df_all = df_all[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack','sum buzz+attack', 'sum']]
    
    print (df_all)

    df_all_norm = df_all.copy()
    for col in df_all_norm.columns[1:]:
        df_all_norm[col] = df_all[col]/df_all['sum'] 

    df_all_norm = df_all_norm[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack','sum buzz+attack', 'sum']]
    print (df_all_norm)

    trail_day = '130819'
    df_all.to_csv(f'{trail_day}_df_all.csv')
    df_all_norm.to_csv(f'{trail_day}_df_norm.csv')


    # vis
    # plt.plot (df_all_norm)
    # plt.show()

    cols = df_all_norm.columns
    cm = np.corrcoef(df_all_norm[cols].values.T)
#sns.set(font_scale=1.5)
    hm = sns.heatmap(cm,
                    cbar=True,
                    annot=True,
                    square=True,
                    fmt='.2f',
                    annot_kws={'size': 9},
                    yticklabels=cols,
                    xticklabels=cols)

    plt.tight_layout()
    # plt.savefig('images/10_04.png', dpi=300)
    plt.show()

    cols = df_all.columns
    cm = np.corrcoef(df_all[cols].values.T)
#sns.set(font_scale=1.5)
    hm = sns.heatmap(cm,
                    cbar=True,
                    annot=True,
                    square=True,
                    fmt='.2f',
                    annot_kws={'size': 9},
                    yticklabels=cols,
                    xticklabels=cols)

    plt.tight_layout()
    # plt.savefig('images/10_04.png', dpi=300)
    plt.show()