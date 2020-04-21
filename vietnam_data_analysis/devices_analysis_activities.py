import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import attr
import seaborn as sns


class DATA:
    """data from one file """
    def __init__(self, fname, color): #color: 1 white, 0 black
        self.fname = fname
        self.color = color
        # self.df = pd.DataFrame()
        self.df = pd.read_csv(self.fname)
        self.df_activity = pd.DataFrame()
        self.trial_date = None

    def add_color (self):
        self.df_activity['color'] = self.color
            
    def time_to_index (self): # need to be fixed in order to use
            """change time column into datetime index"""
            # self.df.index = pd.TimedeltaIndex(self.df['time'])
            #for files with no "time" column:
            self.df.rename(columns={'Unnamed: 0':'time'}, inplace=True)
            self.df.index = pd.TimedeltaIndex(self.df['time'])
            # self.df.index = pd.to_datetime(self.df['time'])
            # #self.df.drop(['time'], axis=1, inplace=True)

    def short_fname (self):
        """shorten fname to file name only and find trial_date"""
        self.fname = self.fname.split('/')
        self.trial_date = self.fname[-2]
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
        # self.df_activity = self.df_activity[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack','social call']]
        self.df_activity = self.df_activity[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack']]
        # print (self.df_activity)

    def sum_activities(self):
        """ sum all activites but search"""
        self.df_activity['sum activities'] = self.df_activity['approach']+self.df_activity['buzz1']+self.df_activity['buzz2']+self.df_activity['attack']
        self.df_activity['sum buzz+attack'] = self.df_activity['buzz1']+self.df_activity['buzz2']+self.df_activity['attack']
        self.df_activity['sum buzzes'] = self.df_activity['buzz1']+self.df_activity['buzz2']
        self.df_activity['sum all']= self.df_activity['search']+ self.df_activity['approach']+self.df_activity['buzz1']+self.df_activity['buzz2']+self.df_activity['attack']
        self.df_activity = self.df_activity[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack', 'sum buzzes','sum buzz+attack','sum activities','sum all']]
    
    def run (self):
        self.short_fname()
        self.time_to_index()
        self.count_activity()
        self.add_color()
        self.find_similar_activities()
        self.sum_activities()

# @attr.s
# class AllFiles:
#     """A unified dataframe.
#     Attributes: df_list, df_all.
#     Methods: merge_df, create_big_data, save_csv, run.
#     """
#     df_list = attr.ib(validator=instance_of(list))
#     df_all = attr.ib(default=pd.DataFrame)
        
    
#       # file_list = [data1,data2,data3,data4,data5,data6]
#     # all_data = []
#     def create_big_data(self) -> None:
#         """Merges all data frames in the list into one big data frame"""
#         basic_df = self.df_list.pop(0)
#         for df in self.df_list:
#             basic_df = pd.concat([basic_df, df], sort = False)
#         self.df_all = basic_df



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
    #color: 1 white, 0 black
    path = '/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/devices_for_analysis/170819/'
    data1 = DATA(f'{path}Data_Frame_8.csv', 1)
    data2 = DATA(f'{path}Data_Frame_13.csv', 1)
    data3 = DATA(f'{path}Data_Frame_15.csv', 1)
    data4 = DATA(f'{path}Data_Frame_25.csv', 0)
    data5 = DATA(f'{path}Data_Frame_28.csv', 0)
    # data6 = DATA(f'{path}Data_Frame_42.csv', 0)

    file_list = [data1,data2,data3,data4,data5]

    # data1 = DATA('Data_Frame_1.csv', 1)
    # data2 = DATA('Data_Frame_18.csv', 0)
    # data3 = DATA('Data_Frame_21.csv', 0)
    # data4 = DATA('Data_Frame_35.csv', 0)
    # data5 = DATA('Data_Frame_41.csv', 1)
    
# organize each file in the list and than combine them all to one df:
    # file_list = [data1,data2,data3,data4,data5,data6]
    all_data = []
    for f in file_list:
        f.run()
        all_data.append(f.df_activity)
        trial_date = f.trial_date
    print (all_data)

#here, combine them all to one df:
    basic_df = all_data.pop(0)
    for df in all_data:
        basic_df = pd.concat([basic_df, df], sort = False)
    df_all = basic_df
    print (df_all)

# #add sums columns:
#     df_all['sum'] = df_all['search']+ df_all['approach']+df_all['buzz1']+df_all['buzz2']+df_all['attack']
#     df_all['sum buzz+attack'] = df_all['buzz1']+df_all['buzz2']+df_all['attack']
#     df_all = df_all[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack','sum buzz+attack', 'sum']]
#     print (df_all)

#normalize df_all:
    df_all_norm = df_all.copy()
    for col in df_all_norm.columns[1:]:
        df_all_norm[col] = df_all[col]/df_all['sum all'] 

    df_all_norm = df_all_norm[['color', 'search', 'approach', 'buzz1', 'buzz2', 'attack', 'sum buzzes','sum buzz+attack','sum activities','sum all']]
    print (df_all_norm)

# save to csv:
    print (trial_date)
#     trial_date = '130819'
    df_all.to_csv(f'{trial_date}_df_all.csv')
    df_all_norm.to_csv(f'{trial_date}_df_norm.csv')


#     # vis correl
   # # plt.plot (df_all_norm)
    ## plt.show()

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