import attr
from attr.validators import instance_of
import pandas as pd
from pathlib import Path
import time
import datetime
from process_GUI_input import *

class FileData:
    """Pipeline to process data of one ID on one design (both fixations and conditions).
    Attributes: fixations, events, id_num, design, df_fixations, df_cond, df_id.
    Methods: create_fixation_df, create_cond_df, merge_df, run count_data.
    """
    def __init__(self, f: TxtFile):
        self.fstart = pd.to_timedelta(f.fstart)
        self.df = pd.DataFrame()
        # self.df_file = pd.read_fwf(f.path, header=None)
        self.df_file = pd.read_csv(f.path, sep="\t", header=None)
        self.experiment = f.experiment
        

    def create_df(self) -> None:
        """Converts file to data frame"""
        df = self.df_file.copy()
        df.columns = ["start_time", "end_time","activity"]
        df['start_time'] = pd.to_timedelta(df['start_time'], unit='s')
        df['start_time'] = df['start_time'] - pd.to_timedelta(df['start_time'].dt.days, unit='d')
        df['end_time'] = pd.to_timedelta(df['end_time'], unit='s')
        self.df = df

    def find_real_time(self):
        self.df['real_start'] = self.fstart+self.df['start_time']
        self.df['real_end'] = self.fstart+self.df['end_time']

    # def count_df(self) -> None:
    #     """Optional function. Does not call by func run(). Incompatible with func merge_df().
    #     Merges conditions and fixations dataframes into one multi-index data frame, 
    #     with the count of time as data, and ID, design and condition as multi-index
    #     """
    #     df = self.df_fixations.merge(self.df_cond, on='time')
    #     df = df.dropna()
    #     df = df.groupby(['condition', 'aveH', 'aveV']).count()
    #     self.df_id = df.reset_index().set_index(['ID', 'design', 'condition'])
    
    def run(self) -> None:
        """Main pipeline"""
        self.create_df()
        self.find_real_time()
    
@attr.s
class AllFiles:
    """A unified dataframe.
    Attributes: df_list, df_all.
    Methods: merge_df, create_big_data, save_csv, run.
    """
    df_list = attr.ib(validator=instance_of(list))
    df_all = attr.ib(default=pd.DataFrame)
    device_num = attr.ib(default=attr.Factory(str))

    def merge_df(self, basic_df: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
        """Appends dataframe given by create_big_data func into one multi-index data frame"""
        df_merge = pd.concat([basic_df, df])
        df_merge = df_merge.dropna()
        return df_merge

    def create_big_data(self) -> None:
        """Merges all data frames in the list into one big data frame"""
        basic_df = self.df_list.pop(0)
        for df in self.df_list:
            basic_df = self.merge_df(basic_df, df)
        # basic_df.index = pd.TimedeltaIndex(basic_df['real_start'])
        basic_df.insert(0, 'time', pd.TimedeltaIndex(basic_df['real_start'])) #new
        # basic_df['time'] = pd.TimedeltaIndex(basic_df['real_start']) #new
        basic_df = basic_df.sort_values(by = ['time'])
        # basic_df.index = pd.TimedeltaIndex(basic_df['time']) #new
        # basic_df.drop ('time', axis=1 ,inplace=True) #new
        # basic_df = basic_df.sort_index()
        self.df_all = basic_df

    def device_number (self):
        self.device_num= self.device_num.split("_")
        self.device_num = self.device_num[-1]
        # print (self.device_num)

    def save_csv(self) -> None:
        """Saves dataframe into csv file"""
        output_file = (f"Data_Frame_{self.device_num}.csv")
        # output_file = (f"Data_Frame_{pd.Timestamp.now().strftime('%Y_%m_%d_%H_%M_%S')}.csv")
        output_dir = Path('Results')
        output_dir.mkdir(parents=True, exist_ok=True)
        self.df_all.to_csv(output_dir / output_file)

    def run(self) -> None:
        """Main pipeline"""
        self.create_big_data()
        self.device_number()
        # self.cond_names()
        self.save_csv()

        
if __name__ == "__main__":
    pass
    