import numpy as np
import pandas as pd

fname = '/Users/gonina/Dropbox/classes/vietnam_workshop/myotis pilosus/all data analysis/to yossi- all activities_24_devices/all_df_all.csv'
df_all = pd.read_csv(fname)

def into_bins(device,minutes='20Min'):
    df = df_all[df_all['device']==device].copy()
    # df_all.index = pd.to_datetime(df_all['time']).dt.time
    df = df.copy().append({'time':'11:30:00'},ignore_index=True)
    df['time'] = pd.TimedeltaIndex(df['time'])
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
result=pd.DataFrame(result)
# result.index = pd.to_datetime(df_all['time']).dt.time
result.to_csv('24_devices_time_bins.csv')
print (result.columns)

# names=['time','activity','date','device','color','location']