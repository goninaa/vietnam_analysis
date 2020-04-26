import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import attr
import seaborn as sns
import re


class DATA:
    """data from one file """
    def __init__(self, fname, color, loc): #color: 1 white, 0 black
        self.fname = fname
        self.color = color
        self.loc = loc
        # self.df = pd.DataFrame()
        self.df = pd.read_csv(self.fname)
        self.df_activity = pd.DataFrame()
        self.trial_date = None

    def add_color (self):
        # self.df_activity['color'] = self.color
        self.df['color'] = self.color

    def add_fname_date (self):
        self.df['device'] = self.fname.split('_')[-1].split('.')[0]
        self.df['date'] = self.trial_date
        self.df['location'] = self.loc
        
            
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

    def activities (self):
        """remove 'empty'"""
        # search = self.df[self.df['activity'].filter(like='search')]
        # self.df = self.df[self.df['activity']=='search']
        # self.df = self.df[self.df['activity'].str.contains("search")]
        self.df['activity'].str.lower()
        # search = self.df['activity'].str.startswith('search') 
        # search = self.df.filter(like='search',axis=0)
        search = self.df['activity'].str.contains('search')
        approach = self.df['activity'].str.contains('approach')
        buzz1 = self.df['activity'].str.contains('buzz1') 
        buzz2 = self.df['activity'].str.contains('buzz2') 
        attack = self.df['activity'].str.contains('attack') 
        # act = self.df['activity'].str.extract(r'([search])(\approach)')
        # df.filter(regex='e$', axis=1)
        # act = self.df['activity'].filter(like = 'search')
        self.df_activity = self.df.loc[search|approach|buzz1|buzz2|attack]
        # self.df = act
        # self.df = self.df.dropna()
        # self.df['activity'] = self.df['activity'].replace(act,'test')
        # self.df['activity'] = self.df['activity'].replace(act,'test')


       

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
    
    def run (self):
        self.short_fname()
        self.time_to_index()
        # self.count_activity()
        self.add_color()
        self.add_fname_date()
        self.activities()
        # self.find_similar_activities()

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
    path = '/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/devices_for_analysis/180819/'
    #180819
    data1 = DATA(f'{path}Data_Frame_7.csv', 0,'c')
    data2 = DATA(f'{path}Data_Frame_9.csv', 0,'f')
    data3 = DATA(f'{path}Data_Frame_14.csv', 0,'b')
    data4 = DATA(f'{path}Data_Frame_36.csv', 1,'a')
#110819
    # data1 = DATA(f'{path}Data_Frame_10.csv',1, 'b')
    # data2 = DATA(f'{path}Data_Frame_22.csv'	,0,'d')
    # data3 = DATA(f'{path}Data_Frame_29.csv'	,0,'a')
    # data4 = DATA(f'{path}Data_Frame_37.csv'	,1,'c')
    # data5 = DATA(f'{path}Data_Frame_40.csv'	,1,'f')
    # data6 = DATA(f'{path}Data_Frame_42.csv'	,0,'e')

    #130819
    # data1 = DATA(f'{path}Data_Frame_1.csv',	1,'a')
    # data2 = DATA(f'{path}Data_Frame_18.csv',0,'b')
    # data3 = DATA(f'{path}Data_Frame_21.csv',0,'c')
    # data4 = DATA(f'{path}Data_Frame_35.csv',0,'f')
    # data5 = DATA(f'{path}Data_Frame_41.csv',1,'e')

#140819
    # data1 = DATA(f'{path}Data_Frame_24.csv',0,'e')
    # data2 = DATA(f'{path}Data_Frame_32.csv',1,'f')
    # data3 = DATA(f'{path}Data_Frame_33.csv',1,'b')
    # data4 = DATA(f'{path}Data_Frame_4.csv',0,'a')
   
   #170819
    # data1 = DATA(f'{path}Data_Frame_13.csv',1,'e')
    # data2 = DATA(f'{path}Data_Frame_15.csv',1,'a')
    # data3 = DATA(f'{path}Data_Frame_25.csv',0,'b')
    # data4 = DATA(f'{path}Data_Frame_28.csv',0,'f')
    # data5 = DATA(f'{path}Data_Frame_8.csv',1,'d')

    # file_list = [data1,data2,data3,data4,data5,data6]
    file_list = [data1,data2,data3,data4]

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
        # all_data.append(f.df)
        all_data.append(f.df_activity)
        trial_date = f.trial_date
    # print (all_data)

#here, combine them all to one df:
    basic_df = all_data.pop(0)
    for df in all_data:
        basic_df = pd.concat([basic_df, df], sort = False)
    df_all = basic_df
    df_all = df_all[['activity','date','device','color','location','time']]
    # print (df_all)
    acts = df_all['activity'].unique()
    print (acts)

    ###part 2
    # df_all = pd.read_csv(fname)

    def into_bins(device,minutes='20Min'):
        df = df_all[df_all['device']==device].copy()
        # df_all.index = pd.to_datetime(df_all['time']).dt.time
        df = df.copy().append({'time':'11:30:00'},ignore_index=True)
        df['time'] = pd.TimedeltaIndex(df['time'])
        # df_bins = df.groupby([pd.Grouper(key='time',base = 30, freq= minutes), 'activity']).size() #working!!!!
        df_bins = df.groupby([pd.Grouper(key='time',base = 30, freq= minutes), 'activity','date','device','color','location']).size() #working!!!!
        # v = df_all.groupby([pd.Grouper(key='time', freq='30min'), 'activity']).size().unstack(fill_value=0) #also working
        # print (df_bins)
        return df_bins

    devices = df_all['device'].unique()
    frames= []
    for device in devices:
        df_bin = into_bins(device)
        frames.append(df_bin)
    result = pd.concat(frames) 
    result.to_csv(f'test_1808.csv')
    print (result)

    # dev_7 = into_bins('7')
    # dev_9 = into_bins('9')
    # dev_14 = into_bins('14')
    
    # print (dev_7)
    # print (dev_9)

    # frames = [dev_7,dev_9]
    # # result = pd.concat(frames, keys=['dev_7','dev_9']) 
    # #here, combine them all to one df:
    # result = pd.concat(frames) 
    # # df.set_index(['time'])
    # print (result)



    # result.to_csv(f'test_1808.csv')
    # print (df_all[df_all['device']=='7'])

    # minutes = '30Min'
    # dev_7 = df_all[df_all['device']=='7']
    # # df_all.index = pd.to_datetime(df_all['time']).dt.time
    # df_all = df_all.copy().append({'time':'11:30:00'},ignore_index=True)
    # df_all['time'] = pd.TimedeltaIndex(df_all['time'])
    # df_bins = df_all.groupby([pd.Grouper(key='time', convention='start',base = 30, freq= minutes), 'activity']).size() #working!!!!
    # # v = df_all.groupby([pd.Grouper(key='time', freq='30min'), 'activity']).size().unstack(fill_value=0) #also working
    # print (df_bins)


    # df_new = pd.DataFrame()
    # df_bins = df_all.resample(minutes, base=base, label='right').count()
    # print (df_bins)
    # for act in acts:
    #     dev_7_time = dev_7[dev_7['activity']==act].resample(minutes, base=base, label='right').count() #good
    #     print (dev_7_time)
    #     df_new.append(dev_7_time['activity'])
   
   
    #     # df_new = pd.concat([df_new, dev_7_time['activity']], sort = False)
    # # df_new['search']= df_new[df_new.columns[0]]
    # # df_new.drop(0,axis=1,inplace=True)

    # print (dev_7_time)
    # print (df_new)



    # minutes = '30Min'
    # base =11
    # dev_7 = df_all[df_all['device']=='7']
    # # print (dev_7)
    # # print (dev_7['activity'].unique)
    # df_all.index = pd.to_datetime(df_all['time']).dt.time
    # # base = df_all.index[0].minute
 
    # dev_7_time = dev_7[dev_7['activity']=='search'].resample(minutes, base=base, label='right').count() #good
    # # 
    # # dev_7_time['search'] = dev_7[dev_7['activity']=='search'].resample(minutes, label='right').count()
    # # df_new = pd.DataFrame( columns=['search', 'number'])
    # df_new = pd.DataFrame()
    # df_new = pd.concat([df_new, dev_7_time['activity']], sort = False)
    # df_new['search']= df_new[df_new.columns[0]]
    # df_new.drop(0,axis=1,inplace=True)
    # # df_new = df_new.rename({0: 'search'}, axis='columns') #works
    # print (dev_7_time)
    # print (df_new)



    # from collections import Counter
    # df_count = Counter(dev_7['activity'])
    # print (df_count)
    # df_count = Counter(dev_7_time['activity'])
    # print (df_count)
