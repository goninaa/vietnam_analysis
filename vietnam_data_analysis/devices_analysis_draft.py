import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import attr
from attr.validators import instance_of

class DATA:
    """data from one file """
    def __init__(self, fname):
        self.fname = fname
        # self.df = pd.DataFrame()
        self.df = pd.read_csv(self.fname)
        self.df_activity = pd.DataFrame()
            
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
        
       
@attr.s
class AllFiles:
    """A unified dataframe.
    Attributes: df_list, df_all.
    Methods: merge_df, create_big_data, save_csv, run.
    """
    df_list = attr.ib(validator=instance_of(list))
    df_all = attr.ib(default=pd.DataFrame)
   

    def merge_df(self, basic_df: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
        """Appends dataframe given by create_big_data func into one multi-index data frame"""
        df_merge = pd.concat([basic_df, df])
        # df_merge = df_merge.dropna()
        return df_merge

    def create_big_data(self) -> None:
        """Merges all data frames in the list into one big data frame"""
        basic_df = self.df_list.pop(0)
        for df in self.df_list:
            basic_df = self.merge_df(basic_df, df)
        self.df_all = basic_df
       

    # def run (self):
    #     self.count_activity()


if __name__ == "__main__":
    data1 = DATA('Data_Frame_4.csv')
    data2 = DATA('Data_Frame_1_fixed.csv')
    data1.run()
    data2.run()
    print (data1.df_activity)
    print (data2.df_activity)

    df_merge = pd.concat([data1.df_activity, data2.df_activity])
    print (df_merge)
    # print (data1.df_activity.name())