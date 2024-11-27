import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta




load_dotenv()
SOURCE_PATH = os.getenv('SOURCE_PATH')
WINDOW_SIZE = os.getenv('WINDOW_SIZE')



def subtract(indice: int, df):
    return df['Ask'][indice] - df['Bid'][indice]
    
def mean(n_window, indice, df, col_name, sec_param):
    low = indice - window[n_window]
    high = indice - winow[n_window + 1]
    if (sec_param):
        return (df[col_name][low:high + 1] - sec_param).mean()
    return (df[col_name][low:high + 1]).mean()
        
def std(low, high, df, col_name):
    low = indice - window[n_window]
    high = indice - winow[n_window + 1]
    return df[col_name][low:high + 1].std()

def max(low, high, df, col_name, sec_param):
    low = indice - window[n_window]
    high = indice - winow[n_window + 1]
    if (sec_param):
        return (df[col_name][low:high + 1] - sec_param).max()
    return df[col_name][low:high + 1].max()

def min(low, high, df, col_name, sec_param):
    low = indice - window[n_window]
    high = indice - winow[n_window + 1]
    if (sec_param):
        return (df[col_name][low:high + 1] - sec_param).min()
    return df[col_name][low:high + 1].min()



df = pd.read_csv(SOURCE_PATH)#[-80000:]
def calculate_minuete(total_time):
    time_item = total_time[1]
    dt = datetime.strptime(time_item, "%H:%M:%S.%f")
    total_minutes = dt.hour * 60 + dt.minute + dt.second / 60
    return total_minutes
    
time_series = df['Local time'].str.split(' ').apply(calculate_minuete)
print(time_series)
