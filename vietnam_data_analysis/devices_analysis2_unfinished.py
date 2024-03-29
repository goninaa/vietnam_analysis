import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import attr
from attr.validators import instance_of


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
            self.df.rename( columns={'Unnamed: 0':'time'}, inplace=True )
            self.df.index = pd.to_datetime(self.df['time'])
            # self.df.drop(['time'], axis=1, inplace=True)

    def short_fname (self):
        """shorten fname to file name only"""
        self.fname = self.fname.split('/')
        self.fname = self.fname[-1]

    def count_activity (self):
        """ """
        self.df_activity = pd.DataFrame(self.df.copy().groupby('activity').count())
        self.df_activity = pd.DataFrame(self.df_activity['time'])
        self.df_activity.rename(columns={"time": f"{self.fname}"}, inplace = True)
        self.df_activity = self.df_activity.transpose()
        # self.df_activity = pd.Series(self.df_activity, name = self.fname)

    def find_similar_activities(self):
        """ unite similar activites names"""
        activites = ['search', 'approach', 'buzz1', 'buzz2', 'attack','social call']
        for activity in activites:
            act = self.df_activity.filter(like=activity)
            self.df_activity[activity] = act.sum(axis=1)
        self.df_activity = self.df_activity[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack','social call']]
        # print (self.df_activity)
    
    def run (self):
        self.short_fname()
        self.time_to_index()
        self.count_activity()
        self.add_color()
        self.find_similar_activities()

@attr.s
class AllFiles:
    """A unified dataframe.
    Attributes: df_list, df_all.
    Methods: merge_df, create_big_data, save_csv, run.
    """
    df_list = attr.ib(validator=instance_of(list))
    df_all = attr.ib(default=pd.DataFrame)
        
    
      # file_list = [data1,data2,data3,data4,data5,data6]
    # all_data = []
    def create_big_data(self) -> None:
        """Merges all data frames in the list into one big data frame"""
        basic_df = self.df_list.pop(0)
        for df in self.df_list:
            basic_df = pd.concat([basic_df, df], sort = False)
        self.df_all = basic_df


class Main:
    """far from finish"""

    def __init__(self, fname, color): #color: 1 white, 0 black
        self.file_list = file_list
        self.all_data = []
        

    # file_list = attr.ib(validator=instance_of(list))
    # all_data = attr.ib(default=list)

    def df_list(self):
        """create list of df"""
        for f in file_list:
            f.run()
            all_data.append(f.df_activity)
        print (all_data)

#    def raw_data(self) -> None:
#         """creates raw data objects for each file"""
#         filelist = ProcessFilelist(self.user_input.filelist)
#         filelist.get_file_attrs()
#         self.txtdict = filelist.txt_dict

    # for f in file_list:
    #     f.run()
    #     all_data.append(f.df_activity)
    # print (all_data)


if __name__ == "__main__":
    path = '/Users/gonina/Dropbox/vietnam-backup/mytois pilosus/excel analysis/devices_for_analysis/110819/'
    data1 = DATA(f'{path}Data_Frame_10.csv', 1)
    data2 = DATA(f'{path}Data_Frame_22.csv', 0)
    data3 = DATA(f'{path}Data_Frame_29.csv', 0)
    data4 = DATA(f'{path}Data_Frame_37.csv', 1)
    data5 = DATA(f'{path}Data_Frame_40.csv', 1)
    data6 = DATA(f'{path}Data_Frame_42.csv', 0)

    file_list = [data1,data2,data3,data4,data5,data6]

    one_day_data = Main(file_list)

    one_day_data.df_list()


    # data1 = DATA('Data_Frame_1.csv', 1)
    # data2 = DATA('Data_Frame_18.csv', 0)
    # data3 = DATA('Data_Frame_21.csv', 0)
    # data4 = DATA('Data_Frame_35.csv', 0)
    # data5 = DATA('Data_Frame_41.csv', 1)


    
# here:
    # file_list = [data1,data2,data3,data4,data5,data6]
    # all_data = []
    # for f in file_list:
    #     f.run()
    #     all_data.append(f.df_activity)
    # print (all_data)

    # data1.run()
    # data2.run()
    # print (data1.df_activity)
    # print (data2.df_activity)

    # all_data = list([data1.df_activity, data2.df_activity])

#here:
    # basic_df = all_data.pop(0)
    # for df in all_data:
    #     basic_df = pd.concat([basic_df, df], sort = False)
    # df_all = basic_df
    # print (df_all)

#     df_all = df_all.fillna(0)
#     df_all['attack'] = df_all['attack']+ df_all['attack?']
#     df_all.drop(['attack?'],axis = 1, inplace = True)
#     # df_all['social call'] = df_all['social call']+ df_all['social calls']
#     # df_all.drop(['social calls'],axis = 1, inplace = True)
#     # df_all['sum'] = df_all.sum(axis=1)
#     # df_all = df_all[['search', 'approach', 'buzz1', 'buzz2', 'attack','social call','empty', 'sum']]

#     df_all.drop(['social calls', 'social call', 'empty'],axis = 1, inplace = True)
#     # df_all['sum'] = df_all.sum(axis=1)
#     df_all['sum'] = df_all['search']+ df_all['approach']+df_all['buzz1']+df_all['buzz2']+df_all['attack']
#     df_all['sum buzz+attack'] = df_all['buzz1']+df_all['buzz2']+df_all['attack']
#     df_all = df_all[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack','sum buzz+attack', 'sum']]
    
#     print (df_all)

#     df_all_norm = df_all.copy()
#     for col in df_all_norm.columns[1:]:
#         df_all_norm[col] = df_all[col]/df_all['sum'] 

#     df_all_norm = df_all_norm[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack','sum buzz+attack', 'sum']]
#     print (df_all_norm)

#     trail_day = '130819'
#     df_all.to_csv(f'{trail_day}_df_all.csv')
#     df_all_norm.to_csv(f'{trail_day}_df_norm.csv')


#     # vis
#     # plt.plot (df_all_norm)
#     # plt.show()

#     cols = df_all_norm.columns
#     cm = np.corrcoef(df_all_norm[cols].values.T)
# #sns.set(font_scale=1.5)
#     hm = sns.heatmap(cm,
#                     cbar=True,
#                     annot=True,
#                     square=True,
#                     fmt='.2f',
#                     annot_kws={'size': 9},
#                     yticklabels=cols,
#                     xticklabels=cols)

#     plt.tight_layout()
#     # plt.savefig('images/10_04.png', dpi=300)
#     plt.show()

#     cols = df_all.columns
#     cm = np.corrcoef(df_all[cols].values.T)
# #sns.set(font_scale=1.5)
#     hm = sns.heatmap(cm,
#                     cbar=True,
#                     annot=True,
#                     square=True,
#                     fmt='.2f',
#                     annot_kws={'size': 9},
#                     yticklabels=cols,
#                     xticklabels=cols)

#     plt.tight_layout()
#     # plt.savefig('images/10_04.png', dpi=300)
#     plt.show()